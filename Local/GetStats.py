#! /usr/bin/python
# GetStats.py

#################
# NOTES & USAGE #
#################

# This python script will retrieve the "summary" stats from a
# BFGMiner API instance, and write them as variables to a PHP
# file on a remote server using SCP.

# I use LaunchD to run this periodically, so I don't have to
# login to pools to check my current hashrate.


###########
# IMPORTS #
###########

import os
import socket
import string


##################
# USER VARIABLES #
##################

HOST_IP = '127.0.0.1'  	# IP of BFGMiner instance to monitor
HOST_PORT = 4028		    # Port # of BFGMiner to monitor


#############
# FUNCTIONS #
#############

def get_bfg_stats():
	try :
		command="summary"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((HOST_IP, HOST_PORT))
		s.send(command)
		output = s.recv(102433)
		s.close()

		output = output.split(',')
		list1 = [i.split('=')[0] for i in output]
		list2 = [i.split('=')[1] for i in output]
		data = []

		for (i, item) in enumerate(list1):
			foo = '$' + item.upper().replace(' ','') + '=\'' + list2[i] + '\';'
			data.append(foo)

		thefile = open('/Users/phraust/Scripts/STATS.php', 'w')
		thefile.write('<?php\n')
		for item in data:
			thefile.write('%s\n' % item)
		thefile.write('?>')
		thefile.close()
		print 'get_bfg_stats() succeded.'
		write_stats()

	except:
		print 'get_bfg_stats() failed.'
		return 0


def write_stats():
	try :
		os.system('scp /path/to/STATS.php user@host:/path/to/STATS.php')
		print 'write_stats() succeeded.'

	except:
		print 'write_stats() failed.'
		return 0


get_bfg_stats()


#####################################
#    Brought to you by Phraust Co.  #
#   "Mining For A Better Tomorrow." #
# 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU #
#####################################
