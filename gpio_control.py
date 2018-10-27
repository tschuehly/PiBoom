#!/usr/bin/env python

from datetime import datetime
import RPi.GPIO as GPIO
import mpd
import time
import os
from subprocess import call

MAIN = 26 #Start/Stop the music
PREV = 13 #Previous Song
NEXT = 6 #Next Song
VOL_DOWN = 5  #Turn down the volume
VOL_UP = 11 #Turn up the volume
SHUT = 9 #Turn Raspberry off
LED1 = 10 #Action indicator LED
GPIO.setmode(GPIO.BCM)
GPIO.setup(MAIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(VOL_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(VOL_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(NEXT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PREV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SHUT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED1, GPIO.OUT)
def stop_start(channel):
	print "Pressed stop_start"
	GPIO.output(LED1,GPIO.HIGH)
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	status = client.status()
	print status['volume']
	if client.status()['state'] in ('play', 'pause'):
		client.pause()
	else:
		client.play()
	time.sleep(0.3)
	GPIO.output(LED1,GPIO.LOW)
def volup(channel):
	print "Pressed volup"
	GPIO.output(LED1,GPIO.HIGH)
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	print client.status()
	status = client.status()
	volume = int(status['volume'])
	add = volume + 10
	client.setvol(add)
	print volume
	time.sleep(0.5)
	GPIO.output(LED1,GPIO.LOW)
def voldown(channel):
	print "Pressed voldown"
	GPIO.output(LED1,GPIO.HIGH)
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	print client.status()
	status = client.status()
	volume = int(status['volume'])
	sub = volume - 10
	client.setvol(sub)
	print volume
	time.sleep(0.5)
	GPIO.output(LED1,GPIO.LOW)
def nexttrack(channel):
	print "Pressed nexttrack"
	GPIO.output(LED1,GPIO.HIGH)
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	print client.status()
	status = client.status()
	volume = int(status['volume'])
	client.next()
	client.play()
	time.sleep(0.5)
	GPIO.output(LED1,GPIO.LOW)
def prevtrack(channel):
	print "Pressed prevtrack"
	GPIO.output(LED1,GPIO.HIGH)
	print str(datetime.now())
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	print client.status()
	status = client.status()
	volume = int(status['volume'])
	client.previous()
	time.sleep(0.5)
	GPIO.output(LED1,GPIO.LOW)
def shutdown(channel):
	print "Pressed shutdown"
	GPIO.output(LED1,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(LED1,GPIO.LOW)
	client = mpd.MPDClient()
	client.connect("localhost", 6600)
	client.stop()
	client.clear()
	client.add("file:/kartenaenderung/shutdown/shutdown.ogg")
	client.play()
	time.sleep(5)
	client.clear()
	client.close()
	call("sudo shutdown -h now", shell=True)
# The GPIO.add_event_detect() line below set things up so that
# when a rising edge is detected on
# GPIO 5, the mpd client stops/starts the Music
GPIO.add_event_detect(MAIN, GPIO.FALLING, callback=stop_start, bouncetime=300)
GPIO.add_event_detect(VOL_UP, GPIO.FALLING, callback=volup, bouncetime=300)
GPIO.add_event_detect(VOL_DOWN, GPIO.FALLING, callback=voldown, bouncetime=300)
GPIO.add_event_detect(NEXT, GPIO.FALLING, callback=nexttrack, bouncetime=300)
GPIO.add_event_detect(PREV, GPIO.FALLING, callback=prevtrack, bouncetime=300)
GPIO.add_event_detect(SHUT, GPIO.FALLING, callback=shutdown, bouncetime=300)
try:
	while True:
		time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
