Python Monitoring Suite [PMS]
=============================

I wanted to put together a suite of scripts for both local and remote hosts to monitor and report on the status of a miner.

Ideally, I'd like it to be able to have it:

* Startup when the system boots, and let me know that it's up via an SMS.
* Be able to locate and distinguish mining hardware on the USB chain.
* Be able to startup BFGMiner and set it mining based on the devices present, and the configuration files available.
* Be able to monitor the health of those mining units, restart BFGMiner if needed, and to SMS me if something has gone wrong.
* Have a remote host monitor that the mining host is online and reachable (via whatever port I'd like), and to SMS me otherwise.
* Have the mining host be able to write statistics to my remote hosts webserver, so that I can check up on the basic information whenever I'd like through my browser.

So far, I've broken out the SMS Messaging (SMS.py) and USB lookup (USB.py) into their own individual scripts which can be called.

I've also cleaned up the original BFGMonitor (BFG_Monitor.py), so it will work.  Just make sure you have all the scripts in the same directoy.

*This is totally a work in progress, and no where near finished.*

REQUIREMENTS
------------

* Python (I'm using 2.7.2 on OSX Lion)
* [pygooglevoice](https://code.google.com/p/pygooglevoice/)
* [Google Voice Account](https://voice.google.com)

*[There is a fix](https://code.google.com/r/bwpayne-pygooglevoice-auth-fix/source/checkout) needed to get Google Voice working.*

BFG_Monitor.py
--------------

Pretty self explanitory in the source comments, just look for the USER VARIABLES:

* PHONE = Phone Number to SMS (eg: 9165217197)
* HOST_IP = IP or HOST of BFGMiner instance to monitor (eg: localhost)
* HOST_PORT = Port # of BFGMiner to monitor (eg: 4028)
* HOST_DEVICES = Number of devices to monitor (eg: 16)
* TIMEOUT = Time in seconds to refresh (eg: 10)

BFG_Monitor.py requires SMS.py to be in the same directory.

*Single SCs are seen as 16 devices, BitForce FPGA singles are seen as one device.*


SMS.py
------

Stand-alone, this one can be run via python, or as an executable if CHMOD'ed.

    python SMS.py phone-number 'message'
    
or:

    chmod +x SMS.py
    ./SMS.py phone-number 'message'
    
Needs two things passed to it:

* phone-number = Phone Number to SMS (eg: 9165217197)
* 'message' = Text to message. Must be wrapped in quotes if more than one word (eg: 'SERVER NEEDS HELP.')

*If you are using BFG_Monitor.py, this needs to be CHMOD'ed.*

USB.py
------

On OSX Lion, will list all of the BFL SC devices I have plugged in as if I had run:

    ls /dev/cu.usb*

*This is a work in progress.*


RUNNING
-------

You'll need to chmod them to executable:

    chmod +x *.py

You can then start it like:

    ./BFG_Monitor.py

It'll refresh for every period you specify, and if the count of live devices is lower than the numbee you listed, it will SMS you until you fix it.


BIG UPS
-------

* Phraust: 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU
* Porlpaul: 1PoLrPXHmd3UZ2b8duU6k19pujA9cpEpSt
