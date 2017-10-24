#!/usr/bin/env python
from itty import *
import json
import pprint
import requests
from bs4 import BeautifulSoup
from six.moves import urllib
import os.path
import sys
import spark
import urllib2


try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = '880bca9aacd145dfb6f8c4c7d7a690cf'




# api info website for Canvas https://canvas.instructure.com/courses/785215
# api documentation for Canvas https://canvas.instructure.com/doc/api/index.html
# general format for requesting url: https://canvas.instructure.com/api/v1/ + path
# example: https://canvas.instructure.com/api/v1/courses?include[]=total_scores  for the request for user's grades

def Authorization():
    	global access_token

def login(): 
	return True

def post_message_data(data):
	messages_url = 'https://api.ciscospark.com/v1/messages'
	sendSparkPOST(messages_url, data)

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
	request.add_header("Authorization", "Bearer "+ "ZDhiZjdlZjUtYmRlNy00OGEzLWE1YWMtNjdiNTUyMTgzZmViMTZhYTQzZWEtZTky")
	contents = urllib2.urlopen(request).read()
	return contents

def get_announcement():
	url = 'https://canvas.instructure.com/api/v1//api/v1/announcements'

	params = {
		'context_codes':'',
		'start_date':'',
		'end_date':'',
		'active_only':''}

	r = requests.get(url, params,headers = {"Authorization":access_token} )
	data = json.loads(r.text)
	title = data['title'], message = data['message']
	output = 'reply message'

def get_classes():

	print("IN GET CLASS FUNCTION")
	course_ids = []
	classes = []
	url = 'https://sjsu.instructure.com/'
	content = urllib.request.urlopen(url).read()
	soup=BeautifulSoup(content,'html.parser')
	tag=soup.body.find(class_="ic-NavMenu-list-item__link")
	for string in tag.string:
	    print(string)
	    msg = "Classes: "
	    msg+= string
	    post_message_data( { "roomId": roomid, "markdown": msg } )

	
	classes_data = {'classes':classes, 'course id': course_ids}

	


	#return classes_data
	return tag


def get_grades():

    classes_data = get_classes() # gets a dict of class data from get_classes()
    ids = classes_data['course id'] # the ids of the classes as a list
    courses = classes_data['classes'] # the class names in a list
    class_and_grade={} # an empty dict for class:grade pairs
    
    for i, cid in enumerate(ids):
        grade_url = 'https://sjsu.instructure.com/courses/%s/grades' % ids[i]
        content = urllib.request.urlopen(grade_url).read()
        soup=BeautifulSoup(content,'html.parser')
        tag=soup.body.find(class_="student_assignment final_grade")
        grade=""
        for string in tag.stripped_strings:
            grade+=(repr(string))
        grade=grade[9]+grade[10]+'%' #orig str is 'total:__%', this returns __%
        class_and_grade[courses[i]]=grade #adds a class:grade pair

	msg = class_and_grade
	post_message_data( { "roomId": roomid, "markdown": msg } )


    return class_and_grade # returns a dict of class:grade pairs

@post('/')
def index(request):
	r = json.loads(request.body)
	if not r:
	    return "True"

	pprint.pprint(r)

	roomid = r['originalRequest']['data']['data']['roomId']
	print roomid

	action = r['result']['action']

	if action == 'get_grades':
		get_grades()

	if action == 'get_classes':
		get_classes()

	if action == 'get_announcement':
		get_announcement()

	return True


if __name__ == "__main__":

	run_itty(server='wsgiref', host='0.0.0.0', port=8080)
