#!/usr/bin/perl
use CGI;

#Check if the password match 
sub password_match
{
	my $returnvalue = 0;
	my $pass1 = $_[0];
	my $pass2 = $_[1];
	if($pass1 eq $pass2)
	{
		$returnvalue=1;
	}
	return $returnvalue;
}
# check if the username already exists
sub username_exists
{
	my $returnvalue = 0;
	my $file_name = $_[0];
	my $user_name = $_[1];
	open(CHECK, "<$file_name");
	@lines = <CHECK>;
	close(CHECK);
	foreach $line (@lines)
	{
		chomp $line;
		my @fields = split "," , $line;
		if($user_name eq $fields[1])
			{
				$returnvalue = 1;
			}
	}
	return $returnvalue;
}
sub failed_registeration
{
	$error_message=$_[0];
	$file='./errorRegistration.html';
	open(HEY, "<$file");
	@lines=<HEY>;
	close(HEY);
	#$theuser = '' unless $theuser;
	print "Content-Type: text/html\n\n";
	foreach $line (@lines)
	{
       		 print $line;
        	if(index ($line,"<div class=\"register\">")!= -1)
       		 {
               		 print " $error_message<br>\n";
       		 }
}
}
my $q = new CGI;
my $theuser = $q->param( 'user' );
my $fullname= $q->param('fullname');
my $password= $q->param('password');
my $confirmpassword= $q->param('confirmpassword');
my $file='members.csv';
my $error_message = '';
if(username_exists($file,$theuser))
{

	$error_message.='user exists already';
	failed_registeration($error_message);
}
elsif(password_match($password,$confirmpassword) == 0)
{
	$error_message.='password doesn\'t match';
	failed_registeration($error_message);
}
else
{
	#create a new user
	open(INFO,">>$file");
	my $line = $fullname . "," . $theuser . "," . $password . "\n";
	print INFO $line;
	close(INFO);
 	 $file='./login.html';
        open(HEY, "<$file");
        @lines=<HEY>;
        close(HEY);
        print "Content-Type: text/html\n\n";
        foreach $line (@lines)
        {
                 print $line;
        
}
}
