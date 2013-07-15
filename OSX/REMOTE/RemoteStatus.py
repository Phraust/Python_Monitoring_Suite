#! /usr/bin/env python2
# RemoteStatus.py

#################
# NOTES & USAGE #
#################

# This is a simple script that tries to open a port on a
# remote server, and will text you if it can't.  I schedule
# it to run every 5 minutes through cron:

# */5 * * * * python2 ~/RemoteStatus.py host:port phonenumber 123456789

# You'll want to chmod +x this file if you want to run it
# on it's own. Simply call it like:

# ./RemoteStatys.py host:port 1234567890

# And it'll send a text to the number if the host doesn't respond.

# Mad props to Motoma: http://motoma.io/basic-server-monitoring-with-python/
# I couldn't have put it together without your awesome article.


###########
# IMPORTS #
###########

from os import system
from socket import socket
from sys import argv
from time import asctime

from googlevoice import Voice
from googlevoice.util import input


#############
# FUNCTIONS #
#############

# Display usage instructions.

def usage():
    print('%s <server-info> <phone-number>\n' % (argv[0]))
    print('\tphone-number\tphone number to send sms\n')


# Check server.

def tcp_test(server_info):
    cpos = server_info.find(':')
    if cpos < 1 or cpos == len(server_info) - 1:
        print('You need to give server info as hostname:port.')
        usage()
        return True
    try:
        sock = socket()
        sock.connect((server_info[:cpos], int(server_info[cpos+1:])))
        sock.close
        return True
    except:
        return False


# Send text message.

def send_error(server_info, phone_number):
    voice = Voice()
    voice.login()

    text = server_info + ' NEEDS HELP. :('

    voice.send_sms(phone_number, text)
    voice.logout()


# Check for Script Arugments.

if __name__ == '__main__':
    if len(argv) != 3:
        print('Wrong number of arguments.')
        usage()
    elif not tcp_test(argv[1]):
        send_error(argv[1], argv[2])


#####################################
#    Brought to you by Phraust Co.  #
#   "Mining For A Better Tomorrow." #
# 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU #
#####################################
