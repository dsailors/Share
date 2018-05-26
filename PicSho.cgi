#!/usr/bin/perl
####################################
##
## 10/25/2018 - Created by Dave Sailors davesailors@yahoo.com
##
##
####################################


$picUrl = "/homecam1";
$picFolder = "../../htdocs/homecam1";


#----------------------

print "Content-type: text/html\n\n";

#require 'auth-lib.pl';
require 'cgi-lib.pl';
&ReadParse;

$startPic = $in{startPic};
if ($startPic eq '') { $startPic = 0; }

$countPic = $in{countPic};
if ($countPic eq '') { $countPic = 40; }

print "start = $startPic <br> \n";
print "count = $countPic <br>\n";

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

#print "Folder = $picFolder <br>\n";

@return = `ls -lt $picFolder 2>&1`;
$totalPic = $#return;

print "<center> <h1>$totalPic pictures in the folder </center></h1> <br>\n";
for ($i = $startPic + 1; $i <= $startPic + $countPic; $i++)
  {
     chop($return[$i]);
     @record = split(/[" "]+/,$return[$i]);
     #print "$i $record[8] <br>\n";

     print " <a href=$picUrl/$record[8]><img src=$picUrl/$record[8] height=80 width=120></a> \n";
  }





















