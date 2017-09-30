#!/usr/bin/env python
from itty import *
import json
import pprint
import jimmy 



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



if __name__ == "__main__": 

	run_itty(server='wsgiref', host='0.0.0.0', port=8080)