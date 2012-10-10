#!/usr/bin/env python

# Google API imports
import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run


# --- BEGIN imports required to run examples from Google Developers API --- #
try:
  from xml.etree import ElementTree # for Python 2.5 users
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import atom
import getopt
import sys
import string
import time
# --- END imports required to run examples from Google Developers API --- #

FLAGS = gflags.FLAGS

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret are copied from the API Access tab on
# the Google APIs Console
FLOW = OAuth2WebServerFlow(
    client_id='223393131219.apps.googleusercontent.com',
    client_secret='YebhsIXTuycOzB1FX7lkVgkN',
    scope='https://www.googleapis.com/auth/calendar',
    user_agent='circle-time') #/YOUR_APPLICATION_VERSION')

# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
storage = Storage('calendar.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  credentials = run(FLOW, storage)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google APIs Console
# to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http,
       developerKey='AIzaSyAlqkUo7Id2Dj5I5JkM7MBn7njoZMthI-4')

class CircleTime(object):
	"""
	docstring for CircleTime

	Created by Olga Botvinnik on ...
	"""
	def __init__(self, arg):
		super(CircleTime, self).__init__()
		self.arg = arg
