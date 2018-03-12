#!/usr/bin/env python

from datetime import datetime
import RPi.GPIO as GPIO
import mpd
import time

MAIN = 5 #Start/Stop the music
NEXT = 6 #Next Song
PREV = 13 #Previous Song
VOL_UP = 17 #Turn up the volume
VOL_DOWN = 27  #Turn down the volume

GPIO.setmode(GPIO.BCM)
GPIO.setup(MAIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(VOL_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(VOL_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PREV, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def stop_start(channel):
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	status = client.status()
	print status['volume']
	if client.status()['state'] in ('play', 'pause'):
		client.pause()
	else:
		client.play()
def volup(channel):
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	print client.status()
	status = client.status()
	volume = int(status['volume'])
	add = volume + 10
	client.setvol(add)
	print volume
def voldown(channel):
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	print client.status()
	status = client.status()
	volume = int(status['volume'])
	sub = volume - 10
	client.setvol(sub)
	print volume
def nexttrack(channel):
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	print client.status()
	status = client.status()
	volume = int(status['volume'])
	client.next()
	client.play()
def prevtrack(channel):
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	print client.status()
	status = client.status()
	volume = int(status['volume'])
	client.previous()

# The GPIO.add_event_detect() line below set things up so that
# when a rising edge is detected on
# GPIO 5, the mpd client stops/starts the Music
GPIO.add_event_detect(MAIN, GPIO.FALLING, callback=stop_start, bouncetime=300)
GPIO.add_event_detect(VOL_UP, GPIO.FALLING, callback=volup, bouncetime=300)
GPIO.add_event_detect(VOL_DOWN, GPIO.FALLING, callback=voldown, bouncetime=300)
GPIO.add_event_detect(NEXT, GPIO.FALLING, callback=nexttrack, bouncetime=300)
GPIO.add_event_detect(PREV, GPIO.FALLING, callback=prevtrack, bouncetime=300)
try:
	while True:
		time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
