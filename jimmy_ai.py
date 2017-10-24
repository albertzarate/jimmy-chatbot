#!/usr/bin/env python
from itty import *
import json
import pprint
import jimmy
import requests
from bs4 import BeautifulSoup
import urllib.request


# api info website for Canvas https://canvas.instructure.com/courses/785215
# api documentation for Canvas https://canvas.instructure.com/doc/api/index.html
# general format for requesting url: https://canvas.instructure.com/api/v1/ + path
# example: https://canvas.instructure.com/api/v1/courses?include[]=total_scores  for the request for user's grades

def Authorization():
    	global access_token

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

	course_ids = []
	classes = []
    url = 'https://sjsu.instructure.com/'
    content = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(content,'html.parser')
    tag=soup.body.find(class_="ic-NavMenu-list-item__link")
    for string in tag.strings
        print(string)
	classes_data = {'classes':classes, 'course id': course_ids}


	return classes_data



def get_grades():

	classes = get_classes()

	ids = classes_data['course id']

	for i, cid in enumerate(ids):
		grade_url = 'https://sjsu.instructure.com/courses/%s/grades' % ids[i]
        content = urllib.request.urlopen(grade_url).read()
        soup=BeautifulSoup(content,'html.parser')
        tag=soup.body.find(class_="student_assignment final_grade")
        for string in tag.strings
            print(string)


@post('/')
def index(request):
	r = json.loads(request.body)
	if not r:
	    return "True"

	pprint.pprint(r)
	return "true"

	action = r['result']['action']

	if action == 'get_grades':
		get_grades()

	if action == 'classes':
		get_classes()

	if action == 'get_announcement':
		get_announcement()


if __name__ == "__main__":

	run_itty(server='wsgiref', host='0.0.0.0', port=8080)
