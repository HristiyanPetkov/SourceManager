package RT::CustomModules::EnrichTickets;
use base 'RT::CustomModules';

use strict;
use warnings;
use DBI;

sub _EnrichTicket {
    my $ticket = shift;

    my $host_name = $ticket->CustomFieldValues('host_name')->First;
    if (defined $host_name) {
        $host_name = $host_name->Content;
    } else {
        $host_name = 'Unknown';
        RT::Logger->warning("Host name is not set for ticket #" . $ticket->id);
    }

    RT::Logger->info("Host name is " . $host_name);

    my $db_file = '/mnt/c/Users/vorte/OneDrive/Desktop/database.db';
    my $dbh = DBI->connect("dbi:SQLite:dbname=$db_file", "", "") or die $DBI::errstr;

    my $sth = $dbh->prepare("
        SELECT sources.type, sources.value, organizations.name AS organization_name
        FROM sources
        JOIN organizations ON sources.organization_id = organizations.id
        WHERE sources.value = ?
    ");
    $sth->execute($host_name);

    if (my $row = $sth->fetchrow_hashref) {
        my $organization_name = $row->{organization_name};

        RT::Logger->info("Organization name: " . $organization_name);

        my $org_custom_field = RT::CustomField->new(RT->SystemUser);
        $org_custom_field->LoadByName(Name => 'Organization');
        $ticket->AddCustomFieldValue(Field => $org_custom_field, Value => $organization_name);
    } else {
        my $org_custom_field = RT::CustomField->new(RT->SystemUser);
        $org_custom_field->LoadByName(Name => 'Organization');
        $ticket->AddCustomFieldValue(Field => $org_custom_field, Value => "Unknown");

        RT::Logger->warning("No organization found for host: " . $host_name);
    }

    $sth->finish if $sth;
    $dbh->disconnect;
}

1;
