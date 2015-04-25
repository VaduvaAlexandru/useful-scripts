#!/usr/bin/perl

use strict;
use warnings;
use diagnostics;
use open ':std', ':encoding(UTF-8)';
use Spreadsheet::ParseExcel;
use Spreadsheet::ParseXLSX;


my $parser   = Spreadsheet::ParseExcel->new();
my $workbook = $parser->parse("input/CGL_5.0_Registration_Template.xls");

if ( !defined $workbook ) {
    die $parser->error(), ".\n";

    my $parser = Spreadsheet::ParseXLSX->new();
    my $workbook = $parser->parse("input/CGL_5.0_Registration_Template.xls");

    if ( !defined $workbook ) {
        die $parser->error(), ".\n";
    }
}

for my $worksheet ( $workbook->worksheets() ) {
    my ( $row_min, $row_max ) = $worksheet->row_range();
    my ( $col_min, $col_max ) = $worksheet->col_range();
    my $line = 0;

    for my $row ( $row_min .. $row_max ) {
        if (($line < $row) and ($line != 0) ) {
            last;
        }

        for my $col ( $col_min .. $col_max ) {
            my $cell = $worksheet->get_cell( $row, $col );
            next unless $cell;

            if ( $cell->value ) {
                print " | ", $cell->value(),       " | ";

                # Do this because the "Requirements" sheet has multiple empty rows
                if ( $cell->value eq "PMS.5.3"  ) {
                    $line = $row;
                }
            }
            else {
                last;
            }
        }
        print "\n";
    }
    print "\n";
}
