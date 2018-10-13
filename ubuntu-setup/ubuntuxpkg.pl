#!/usr/bin/perl -w

use strict;
use Carp;

my @pkg_required;
my @pkg_installed;
my $datafile='package.list';
my $found=0;

#--------------------------------------------------
sub get_required_packages {
	open my $handle, '<', 'package.list';
	chomp(@pkg_required = <$handle>);
	close $handle;

	foreach my $line (@pkg_required) {
		$line =~ s/\n//g;
	}
}

#--------------------------------------------------
sub get_installed_packages {
	@pkg_installed=`dpkg --get-selections | grep install | grep -v deinstall | gawk -e '{print \$1}'`;

	foreach my $line (@pkg_installed) {
		$line =~ s/\n//g;
	}
}

#--------------------------------------------------
sub create_data_file {
	unless(-e $datafile) {
		print "   --> generare fisier de date: $datafile\n";
		my $result=`dpkg --get-selections | grep install | grep -v deinstall | gawk -e '{print \$1}' > $datafile`; 

		exit 0;
	}
}

print "Verificare sistem\n";

create_data_file();
print "   --> procesare fisier de date: $datafile\n";
get_required_packages();

foreach my $pkg (@pkg_required){
	if($found==0){
		print "   --> regenerare lista pachete\n";
		get_installed_packages();
	}
	$found=0;

	foreach my $pkginst (@pkg_installed){
		if($pkg eq $pkginst){
			$found=1;
			last;
		}
	}
	if($found == 0){
		system("aptitude install -q -y $pkg\n");
	}
}
