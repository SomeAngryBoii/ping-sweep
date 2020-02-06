use Net::Ping;

$p = Net::Ping->new("icmp");
my $ip_address = '10.11.1.';
my @octet = (1..255); 

for my $i (@octet){
  my $host = $ip_address . $i;

  if($p->ping($host, 2)){
    print "$host  active \n";
  }else{
    print "$host  inactive \n";
  }
}
