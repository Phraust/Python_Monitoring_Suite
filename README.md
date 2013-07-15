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

*My OSX setup is working, I just need to document everything.*


BIG UPS
-------

* Phraust: 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU
* Porlpaul: 1PoLrPXHmd3UZ2b8duU6k19pujA9cpEpSt
