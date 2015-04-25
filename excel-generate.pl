#!/usr/bin/perl

use strict;
use warnings;
use utf8;
use Text::Iconv;
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

print "Sheets = ", $workbook->worksheet_count(), "\n";

for my $worksheet ( $workbook->worksheets() ) {
    my ( $row_min, $row_max ) = $worksheet->row_range();
    my ( $col_min, $col_max ) = $worksheet->col_range();

    for my $row ( $row_min .. $row_max ) {
        for my $col ( $col_min .. $col_max ) {
            my $cell = $worksheet->get_cell( $row, $col );
            next unless $cell;

            print "Row, Col    = ($row, $col)\n";
            print "Value       = ", $cell->value(),       "\n";
            print "Unformatted = ", $cell->unformatted(), "\n";
            print "\n";
        }
    }
}
