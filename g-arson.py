#!/usr/bin/env python

"""
	This is pretty awful in every way, shape, and form.
	But it is an HTTP proxy that swaps every instance 
	of "there", "their", and "they're".
"""

import SocketServer
import SimpleHTTPServer
import urllib
import random
import re
try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO

PORT = 1234

def targetWord(w):
	if( not isinstance(w, basestring) ):
		return False
	w = w.lower()
	if( w == "there" or w == "their" or w == "they're" ):
		print "Found target"
		return True
	return False

def getRandomSub(upper):
	t = ""
	if( upper ):
		t = "T"
	else:
		t = "t"
	r = random.randint(0, 2)
	if( r == 0 ):
		return t + "here"
	if( r == 1 ):
		return t + "hey're"
	if( r == 2 ):
		return t + "heir"

class Proxy(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		f = StringIO()
		data = urllib.urlopen(self.path).read()
		words = re.split(r"([\s,\.]+)", data)
		data = ""
		for x in range(0, len(words)):
			if( targetWord(words[x]) ):
				if( words[x][0] == "T" ):
					words[x] = getRandomSub(True)
				else:
					words[x] = getRandomSub(False)
			if( isinstance(words[x], basestring) ):
				data = data + words[x]
		f.write(data)
		f.seek(0)
		self.copyfile(f, self.wfile)

random.seed()
class LocalSocketServer(SocketServer.ForkingTCPServer):
	allow_reuse_address = True
httpd = LocalSocketServer(('', PORT), Proxy)
print "Starting proxy server (port " + str(PORT) + ")..."
httpd.serve_forever()
