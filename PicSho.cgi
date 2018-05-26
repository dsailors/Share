#!/usr/bin/perl
####################################
## Show / Manage lists home
##
## 11/20/2011 - Created by Dave Sailors davesailors@yahoo.com
##
## 09/03/2012 - Added Security
##
##
####################################



#$picFolder = "../../htdocs/homecam1";
$picUrl = "/homecam1";
$picFolder = "../../htdocs/homecam1";




#----------------------

print "Content-type: text/html\n\n";

#require 'auth-lib.pl';
require 'cgi-lib.pl';
&ReadParse;

#-----------------------------
$year=`date +%Y`; chop($year);
$month=`date +%m`;chop($month);
$day=`date +%d`;  chop($day);
$hour=`date +%H`; chop($hour);
$min=`date +%M`;  chop($min);
$sec=`date +%S`;  chop($sec);
$tstamp = "$year.$month.$day.$hour.$min.$sec";
$tstampfull = "$year\/$month\/$day $hour:$min:$sec";
#-----------------------------
$host=`hostname`;
chop($host);
$PID=$$;
#-----------------------------

print "$0 is starting at $tstampfull<br>\n";

print "Folder = $picFolder <br>\n";

@return = `ls -lt $picFolder 2>&1`;

print "return = $#return <br>\n";

#for ($i = 1; $i <= $#return; $i++)

for ($i = 1; $i <= 10; $i++)
  {
     chop($return[$i]);
     print "$return[$i] <br>\n";
     @record = split(/[" "]+/,$return[$i]);
     print "$i $record[8] <br>\n";
     print " $picFolder/$record[8]<br>\n";

     $check = `ls -al $picUrl/$record[8] 2>&1`;
     print "heck = $check <br>\n";
     print " <img src=$picUrl/$record[8] height=40 width=35> <br>\n";
  }

