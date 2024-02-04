use strict;
use warnings;
use lib '.';

require 'EnrichTickets.pm';

my $dummy_ticket = {
    id    => 123,
    Queue => 'General',
    CustomFields => { host_field => '192.168.10.1' },
};

_EnrichTicket($dummy_ticket);

print "Updated Ticket:\n";
print "ID: ", $dummy_ticket->{id}, "\n";
print "Queue: ", $dummy_ticket->{Queue}, "\n";
print "CustomFields:\n";
foreach my $field (keys %{ $dummy_ticket->{CustomFields} }) {
    print "  $field: ", $dummy_ticket->{CustomFields}->{$field}, "\n";
}
