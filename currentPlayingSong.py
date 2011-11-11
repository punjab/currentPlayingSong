#!/usr/bin/env python
# encoding: utf-8
"""
currentPlayingSong.py

Created by Arvinder Singh Kang on 2011-11-11.
Copyright (c) 2011 Arvinder Singh Kang. All rights reserved.
"""

import sys, os
from lxml import etree
import urllib2
from StringIO import StringIO

def getNowPlaying(url):
	"""
	GET and read XML file
	"""
	# Comment if a remote url for xml
	f = open(url)
	xml = f.read()
	f.close()
	
	# uncomment if a remote url for xml
	# request = urllib2.Request(url)
	# try:
	# 	response = urllib2.urlopen(request)
	# except URLError, e:
	# 	print e.reason	
	# xml = response.read()

	
	"""
	Parse and read first song
	"""
	tree = etree.parse(StringIO(xml))
	# Just the top song
	songEvent = tree.xpath('//EventData[@INDEX=0]')
	# Store in a dictory to sort
	currentSong_dict = {}
	# I need only the top song hence index 0
	for child in songEvent[0]:
		if child.tag == "RadioText":
			currentSong_dict["Title"] = child.text
		elif child.tag == "Artist":
			currentSong_dict[child.tag] =  child.text
		elif child.tag == "Album":
			currentSong_dict[child.tag] =  child.text
		elif child.tag == "Duration":
			currentSong_dict["Time"] =  child.text
	
	# Write nicecast file
	f=open('~/Library/Application Support/Nicecast/NowPlaying.txt', 'w')
	for tag, value in currentSong_dict.items():
		f.write(tag + ": " + value + '\n')
	f.close
		
if __name__ == '__main__':
	# remote file. Remember to uncomment code in getNowPlaying()
	# getNowPlaying('http://www.your/xml/file/url/streaming.xml')
	
	# xml file on disk
	getNowPlaying('streaming.xml')