#!/usr/bin/perl

use Data::Dumper;


open(DATA, "<", $ARGV[0])
      or die "cannot open < input.txt: $!";

#@values=unpack("a6l4H174H*",<DATA>);
@values=unpack("a6 l s s s",<DATA>);

$offset=$values[3];
$rec_number=$values[4];
@values=unpack("H152H*",<DATA>);

print Dumper(@values);

