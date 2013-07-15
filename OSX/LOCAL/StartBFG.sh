#!/bin/sh
#StartBFG.sh

#################
# NOTES & USAGE #
#################

# This is a simple shell script for starting up BFGMiner in a
# GNU screen instance. Make sure you have the appropriate
# settings in your bfgminer.conf setup, and you can add any
# other switches or options to the command below as needed.
# (e.g. --api-listen, etc)

# I've had to define the complete path for all executables,
# since OSX uses LaunchD, which doesn't have any PATHs defined.


/opt/local/bin/screen -Sdm BFGMINER /usr/local/bin/bfgminer -c /path/to/bfgminer.conf


#####################################
#    Brought to you by Phraust Co.  #
#   "Mining For A Better Tomorrow." #
# 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU #
#####################################
