#!/usr/bin/env perl

use Mojolicious::Lite;

get '/' => sub {
    shift()->render(json => {message => 'Hello world.'});
};

app->start;
