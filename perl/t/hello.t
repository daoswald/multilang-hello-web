#!/usr/bin/env perl

use strict;
use warnings;
use Test::More;
use Test::Mojo;
use FindBin qw($Bin);

my $t = Test::Mojo->new(Mojo::File->new("$Bin/../hello.pl"));

$t->get_ok('/')
    ->status_is(200)
    ->json_is('/message' => 'Hello world.');

done_testing();
