#! /usr/bin/python
# SMS.py

#################
# NOTES & USAGE #
#################

# You'll want to chmod +x this file so you can run it.

# Simply call it like ./SMS.py 1234567890 'TEXT MASSAGE'
# to send a text to the number.


###########
# IMPORTS #
###########

from sys import argv
from googlevoice import Voice
from googlevoice.util import input

#############
# FUNCTIONS #
#############

# Display usage instructions.

def usage():
  print('%s Phone-Number \'Message Text\'\n' % (argv[0]))
	print('\tPhone-Number    \tEG: 8081234567')
	print('\t\'Message-Text\'    \tMust be wrapped in quotes.\n')

	return 0

# SMS Function

def send_sms(PHONE, MESSAGE):
	voice = Voice()

	voice.login()
	voice.send_sms(PHONE, MESSAGE)
	voice.logout()

	return 1

# Check for Script Arugments.

if __name__ == '__main__':
	if len(argv) != 3:
		print('Wrong number of arguments.')
		usage()
	else:
		send_sms(argv[1], argv[2])

#####################################
#    Brought to you by Phraust Co.  #
#   "Mining For A Better Tomorrow." #
# 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU #
#####################################
