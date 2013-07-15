#! /bin/sh
# CheckBFG.sh

#################
# NOTES & USAGE #
#################

# This shell script simple checks to makes sure an instance of
# BFGMiner is running, based on the StartBFG.sh that we use.

# Make sure you change the number on the last line to the number
# you want to recieve messages at.

# I've had to define the complete path for all executables,
# since OSX uses LaunchD, which doesn't have any PATHs defined.


if /bin/ps -ef | /usr/bin/grep -v grep | /usr/bin/grep BFGMINER ; then
  exit 0
else
  /Users/phraust/Mining/StartBFG.sh
  /Users/phraust/Scripts/SMS.py 1234567890 'BFGMINER RESTARTED.'
  exit 1
fi


#####################################
#    Brought to you by Phraust Co.  #
#   "Mining For A Better Tomorrow." #
# 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU #
#####################################
