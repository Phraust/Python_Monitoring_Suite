#! /usr/bin/python

###########
# IMPORTS #
###########

import subprocess

DEV_LOC= 'ls /dev/cu.usb*'

p = subprocess.Popen(DEV_LOC , shell=True , stdout=subprocess.PIPE , stderr=subprocess.PIPE)

DEVICES = p.stdout.readlines()
DEVICES = [item.strip() for item in DEVICES]

print DEVICES
print len(DEVICES)

#####################################
#    Brought to you by Phraust Co.  #
#   "Mining For A Better Tomorrow." #
# 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU #
#####################################
