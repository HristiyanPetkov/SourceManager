# package RT::CustomModules::EnrichTickets;
# use base 'RT::CustomModules';

use strict;
use warnings;
use DBI;

sub _EnrichTicket {
    my $ticket = shift;

    my $host_name = $ticket->{CustomFields}->{host_field};

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

        $ticket->{CustomFields}->{Organization} = $organization_name;

        $ticket->{Comments} ||= [];
        push @{$ticket->{Comments}}, {
            Creator  => 'System',
            Content  => "Enriched ticket with organization information: $organization_name",
            Created  => 'now',
            Type     => 'Create',
            ObjectType => 'RT::Ticket',
        };

        $ticket->{Status} = 'resolved';
    } else {
        print "No organization found for host: $host_name\n";
    }

    $sth->finish if $sth;
    $dbh->disconnect;
}

1;
