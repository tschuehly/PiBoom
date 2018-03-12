# toddleplayer_gpio

This extension is based on the idea of [PiBoom](https://github.com/beakersoft/PiBoom).

You can control MusicBox via GPIO buttons on the Raspberry Pi.

First you have to install Python MPD2
```
pip install python-mpd2
```
The easiest way to start the script on startup is to append the following lines to the /etc/rc.local.

```
/PATH_TO/start.sh 2>&1 | tee /PATH_TO/start.log
```

then you create one start.sh and start.log in a desired folder and paste this into the start.sh
```
#!/bin/bash
sleep 30
python /PATH_TO/gpio_control.py &
```
