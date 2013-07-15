Python Monitoring Suite [PMS]
=============================

These files are used to remotely monitor your mining server, and for displaying statistics via a webpage.


RemoteStatus.py
---------------

This is a python script that will try to connect to a remote host's port, and if it fails will send an SMS.

It can be used like this:

    ./RemoteStatus.py host:port phonenumber
    

HTML/
-----

These are the files needed on the remote host's web server for parsing the STATS.php that gets written by the mining host.

Just copy them where you'd like them, and make sure you update the mining server's scripts to point to the appropriate paths.


BIG UPS
-------

* Phraust: 1nbTFZTFy8Wtbti3LhnLFZgd5YTBrXjaU
* Porlpaul: 1PoLrPXHmd3UZ2b8duU6k19pujA9cpEpSt
* Motomoa: http://motoma.io/
