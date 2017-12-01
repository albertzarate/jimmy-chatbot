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

def get_assignments(access_token, date_t, roomid):
    msg = "Checking.... "
    post_message_data( { "roomId": roomid, "markdown": msg } )

    course_info = helper_classes(access_token)
    canvas_a = CanvasAPI(access_token, base_url = 'http://sjsu.instructure.com', api_prefix='/api/v1')
    a_num = 0
    for course_id in course_info['c_ids']:
        assignments = canvas_a.get_assignments(course_id)
        for obj in assignments:
            c_date1 = obj['due_at']
            c_date = str(c_date1)
            if c_date != None:
                if c_date[0] != 'N':
                    print c_date[0:10]
                    print str(date_t)
                    if c_date[0:10] == str(date_t):
                        print a_num
                        print course_id
                        a_num = a_num + 1
    msg = "Number of Assignments due Today: "
    msg += str(a_num)

    post_message_data( { "roomId": roomid, "markdown": msg } )

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

def get_announcements(roomid):
    canvas_an = CanvasAPI(access_token, base_url = 'https://sjsu.instructure.com', api_prefix='/api/v1')
    anns = canvas_an.get_announcements()

    print anns

    print anns['title']
    print anns['message']

    msg = "Title: "
    msg += str(anns['title'])
    msg += "  Message: "
    msg += str(anns['message'])
    
    post_message_data( { "roomId": roomid, "markdown": msg } )

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
