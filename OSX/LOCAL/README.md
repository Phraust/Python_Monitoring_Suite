Python Monitoring Suite [PMS]
=============================

These files are used locally on your mining server to check the status of BFGMiner instances, and to restart them and text you accordingly if BFGMiner should fail.  There is also a script that will write BFGMiner statistics to a remote server for viewing via a webpage.


CheckBFG.sh
-----------

This shell script simple checks to makes sure an instance of BFGMiner is running, based on the StartBFG.sh that we use.

Make sure you change the number on the last line to the number you want to recieve messages at.

*I've had to define the complete path for all executables, since OSX uses LaunchD, which doesn't have any PATHs defined.*


GetStats.py
-----------

This python script will retrieve the "summary" stats from a BFGMiner API instance, and write them as variables to a PHP file on a remote server using SCP.

I use LaunchD to run this periodically, so I don't have to login to pools to check my current hashrate.



Reboot.sh
---------

I use LaunchD to call this script whenever my server reboots, and to text me.


SMS.py
------

You'll want to chmod +x this file so you can run it.

Simply call it like:

    ./SMS.py 1234567890 'TEXT MASSAGE'

to send a text to the number.  If your text is more than one word, wrap it in quotes (e.g. 'SERVER NEEDS HELP.')


StartBFG.sh
-----------

This is a simple shell script for starting up BFGMiner in a GNU screen instance. Make sure you have the appropriate settings in your bfgminer.conf setup, and you can add any other switches or options to the command below as needed (e.g. --api-listen, etc).

*I've had to define the complete path for all executables, since OSX uses LaunchD, which doesn't have any PATHs defined.*


LaunchD/
--------

These files are required to use LaunchD, OSX's replacement for cron.  It's a pain in the ass, so you might want to read up a little bit on it first.


BIG UPS
-------

* Phraust: 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU
* Porlpaul: 1PoLrPXHmd3UZ2b8duU6k19pujA9cpEpSt
* Motomoa: http://motoma.io/
