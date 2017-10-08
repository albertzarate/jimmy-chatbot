#!/usr/bin/env python
from itty import *
import json
import pprint
import jimmy 
import requests

# api info website for Canvas https://canvas.instructure.com/courses/785215
# api documentation for Canvas https://canvas.instructure.com/doc/api/index.html
# general format for requesting url: https://canvas.instructure.com/api/v1/ + path
# example: https://canvas.instructure.com/api/v1/courses?include[]=total_scores  for the request for user's grades

@post('/')
def index(request):
	global r = json.loads(request.body)
	if not r:
	    return "True"

	pprint.pprint(r)
	return "true"

	action = r['result']['action']

	if action == 'get_grades':
		get_grades()

	if action == 'get_announcement':
    	get_announcement()

def get_announcement():
	url = 'https://canvas.instructure.com/api/v1//api/v1/announcements'
	params = dict(
		context_codes= ''
		start_date = ''
		end_date = ''
		active_only = ''
	)
	r = requests.get(url, params,headers = {"Authorization":access_token} )
	data = json.loads(r.text)
	title = data['title'], message = data['message']
	output = 'reply message'

def Authorization():
    	global access_token




if __name__ == "__main__": 

	run_itty(server='wsgiref', host='0.0.0.0', port=8080)
	