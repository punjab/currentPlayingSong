## currentPlayingSong.py

A quick hack in Python to add meta data to the outgoing Radio Station stream.

An XML parser fetches XML feed generated from Radio Software, parses it and writes to a file, that is constantly being read by [Nicecast Studio](http://rogueamoeba.com/nicecast/).

Runs every 1 minute using crontab/launchAgent and writes to the Nowplaying.txt file in a format required by Nicecast streaming server. 