#!/usr/bin/perl

use CGI;

$q = new CGI;
if (defined($q->param('Hacker'))) {
    print $q->header(-type=>'image/bmp');
    open(HACKER,"h".$q->param('Hacker'));
    open(MUSTACHE,"m".$q->param('Mustache'));
    open(SHADES,"s".$q->param('Shades'));

    while (read(HACKER,$hackerb,1)) {
        read(MUSTACHE,$mustacheb,1);
        read(SHADES,$shadesb,1);
        print (chr (ord($hackerb) & ord($mustacheb) & ord($shadesb)));
    }
}
