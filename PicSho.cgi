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
if ($countPic eq '') { $countPic = 42; }


$nextStartPic = $startPic + $countPic;

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



$dusk = `du -sk $picFolder 2>&1`;
@temp = split(/["\t"]+/,$dusk);
$size = $temp[0];

@return = `ls -lt $picFolder 2>&1`;
$totalPic = $#return;

print "xx $return[$nextStartPic] <br>\n";

# - Name read and parse
#@lsrec  = split(/[' ']+/,$return[$nextStartPic]);
#@LR = split(/[-]+/,$lsrec[8]);
#print "left = $LR[0] <br> \n";
#print "right = $LR[1] <br> \n";

print "<center> <h3>$totalPic pictures, Size = $size kb,  </center></h3>\n";

print "<a href=PicSho.cgi?startPic=$nextStartPic&countPic=$countPic > xxxxxxxx</a> <br> \n";
print "start = $startPic , count = $countPic <br>\n";

for ($i = $startPic + 1; $i <= $startPic + $countPic; $i++)
  {
     chop($return[$i]);
     @record = split(/[" "]+/,$return[$i]);
     #print "$i $record[8] <br>\n";

     print " <a href=$picUrl/$record[8]><img src=$picUrl/$record[8] height=80 width=120></a> \n";
  }





















