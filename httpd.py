#!/usr/bin/python

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import os

os.chdir('_site')

server_address = ('127.0.0.1', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()

