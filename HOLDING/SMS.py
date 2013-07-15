#! /usr/bin/python
# SMS.py

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

# SMS Function

def send_sms(PHONE, MESSAGE):
    voice = Voice()
    
    voice.login()
    voice.send_sms(PHONE, MESSAGE)
    voice.logout()

# Check for Script Arugments.

if __name__ == '__main__':
    if len(argv) != 3:
        print('Wrong number of arguments.')
        usage()
    else:
        send_sms(argv[1], argv[2])
        return 1

#####################################
#    Brought to you by Phraust Co.  #
#   "Mining For A Better Tomorrow." #
# 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU #
#####################################
