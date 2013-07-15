#! /usr/bin/python

###########
# IMPORTS #
###########

import datetime
import decimal
import os
import socket
import string
import subprocess
import time


##################
# USER VARIABLES #
##################

PHONE = '(123)456-7890'  	# Phone Numnber to Message

HOST_IP = '127.0.0.1'		# IP of BFGMiner instance to monitor
HOST_PORT = 4028		# Port # of BFGMiner to monitor
HOST_DEVICES = 64		# Number of devices to monitor

TIMEOUT = 10			# Time in seconds to refresh


###################
# MISC. VARIABLES #
###################

class b:
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	CLEAR = '\033[0m'

count = 0


#############
# FUNCTIONS #
#############

# Clears screen between refreshes.

def cls():
	os.system(['clear','cls'][os.name == 'nt'])

# Sends SMS

def send_sms(MESSAGE):
	TEXT = "\'"+MESSAGE+"\'"
	subprocess.call(['./SMS.py', PHONE, TEXT])

# Checks live devices, returns how many are alive.

def get_live_devices():
	try :
		command="devs"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST_IP, HOST_PORT))
		s.send(command)
		data = s.recv(102433)
		s.close()
		return string.count(data, "Alive")
	except:
		return 0

# Reboots Miner, returns how many are alive.

def reboot_miner():
	try:
		command="restart"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST_IP, HOST_PORT))
		s.send(command)
		data = s.recv(102433)
		s.close()
	except:
		return 0


############
# START UP #
############

cls()
print "CHECKING FOR [" + b.BLUE + str(HOST_DEVICES) + b.CLEAR + "] DEVICES."
print "CHECKING HOST ["  + b.BLUE + str(HOST_IP) + ":" + str(HOST_PORT) + b.CLEAR + "]."
print "RECHECKING EVERY [" + b.BLUE + str(TIMEOUT) + b.CLEAR + "] SECONDS."


########
# LOOP #
########

while(1):
	time.sleep(TIMEOUT)
	try:
		if (get_live_devices() < HOST_DEVICES):
			cls()
			count=0
			reboot_message = "MINER IS REBOOTING." , str(get_live_devices()) , "OUT OF" , str(HOST_DEVICES) , "RUNNING."
			send_sms(reboot_message)
			reboot_miner()
			print b.RED + "TEXT SENT. MINER IS REBOOTING." + b.CLEAR
		else:
			cls()
			count += 1
			print "MINER IS OKAY. " + b.GREEN + str(get_live_devices()) + b.CLEAR , "OUT OF" , b.BLUE + str(HOST_DEVICES) + b.CLEAR , "RUNNING FOR" , b.BLUE + str(round((count*TIMEOUT)/60.00/60.00, 2)) + b.CLEAR , "HOURS."
	except:
		cls()
		count=0
		send_sms('MINER IS DEAD.')
		print b.RED + "TEXT SENT. MINER IS DEAD." + b.CLEAR


#####################################
#    Brought to you by Phraust Co.  #
#   "Mining For A Better Tomorrow." #
# 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU #
#####################################
