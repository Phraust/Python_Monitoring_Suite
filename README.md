Python Monitoring Suite [PMS]
=============================

I wanted to put together a suite of scripts for both local and remote hosts to monitor and report on the status of a miner.
So far, I've managed to get the following working:

* Startup when the system boots, and let me know that it's up via an SMS.
* Be able to startup BFGMiner and set it mining.
* Be able to monitor whether BFGMiner has quit silently (which it has in the past), and if so, to text me and restart it.
* Have a remote host monitor that the mining host is online and reachable (via whatever port I'd like), and to SMS me otherwise.
* Have the mining host be able to write statistics to my remote hosts webserver, so that I can check up on the basic information whenever I'd like through my browser without having to login to whatever mining pool.

*This actually kinda works. I've been running it for the last few days, and it seems to be fine.*


BIG UPS
-------

* Phraust: 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU
* Porlpaul: 1PoLrPXHmd3UZ2b8duU6k19pujA9cpEpSt
* Motomoa: http://motoma.io/
