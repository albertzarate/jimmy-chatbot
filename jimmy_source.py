#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itty import *
import json
import pprint
import requests
from bs4 import BeautifulSoup
from six.moves import urllib
import urllib2
from canvas_api import CanvasAPI


def sendSparkPOST(url, data):
	"""
	This method is used for:
	    -posting a message to the Spark room to confirm that a command was received and processed
	"""

	# need to make sure that data is no longer than the spark POST limit
	# of 7439 characters (before encryption).

	if data:
	    if data.get("markdown") and len(data.get("markdown")) > 7400:
	        data["markdown"] = ( data.get("markdown")[:7400] + "...[truncated]" )

	    if data.get("text") and len(data.get("text")) > 7400:
	        data["text"] = ( data.get("text")[:7400] + "...[truncated]" )

	request = urllib2.Request(url, json.dumps(data),
	                        headers={"Accept" : "application/json",
	                                 "Content-Type":"application/json"})
	request.add_header("Authorization", "Bearer "+ "MTZmZDY2ZDMtZmZlNi00Y2U3LWJmYjUtZDQ2YTZiOGVmMzZhYTFmOWVkZjktOTg4")
	contents = urllib2.urlopen(request).read()
	return contents

def post_message_data(data):
	messages_url = 'https://api.ciscospark.com/v1/messages'
	sendSparkPOST(messages_url, data)

def helper_classes(access_token):
    canvas1 = CanvasAPI(access_token, base_url = 'https://sjsu.instructure.com', api_prefix='/api/v1')
    

    courses = canvas1.get_courses()
    pprint.pprint(courses)

    classes = {}
    classes = []
    ids = []
    for course in courses: 
        try:
            name = course['course_code']
            c_id = course['id']
            classes.append(name)
            ids.append(c_id)
        except:
            pass
    
    print classes
    print ids

    course_info = {'course':classes, 'c_ids': ids}
    return course_info
	
def get_classes(access_token, roomid):
    canvas1 = CanvasAPI(access_token, base_url = 'https://sjsu.instructure.com', api_prefix='/api/v1')
    

    courses = canvas1.get_courses()
    pprint.pprint(courses)

    classes = {}
    classes = []
    ids = []
    for course in courses: 
        try:
            name = course['course_code']
            c_id = course['id']
            classes.append(name)
            ids.append(c_id)
        except:
            pass
    
    print classes
    print ids
    
    msg = "Courses:"
    for c in classes:
        msg += ' '
        msg += c
        msg += ' '

    post_message_data( { "roomId": roomid, "markdown": msg } )

    course_info = {'course':classes, 'c_ids': ids}
    return course_info

@post('/')
def index(request):
    r = json.loads(request.body)
    if not r:
        return "True"

    action = r['result']['action']
    
    roomid = r['originalRequest']['data']['data']['roomId']

    if action == 'get_classes':
        username = r['result']['parameters']['username']
        get_classes(access_token, roomid)
    
    if action == 'get_assignments':
        date_t = r['result']['parameters']['date']
        get_assignments(access_token, date_t, roomid)

    if action == 'get_announcements':
        get_announcements(roomid)


if __name__ == "__main__":

	run_itty(server='wsgiref', host='0.0.0.0', port=8000)
