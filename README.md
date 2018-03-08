# toddleplayer_gpio

This extension is a modifided version of [PiBoom](https://github.com/beakersoft/PiBoom).

You can control MusicBox via GPIO buttons on the Raspberry Pi.
I removed the Rotary Control.

Notes

Install the raspery pi GPIO python module
PiBoomControlService makes it run as a service on startup - sudo /etc/init.d/PiBoomControlService.sh status/stop/start
pip install python-mpd2
