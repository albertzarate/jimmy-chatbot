#!/usr/bin/env python
from itty import *
import json
import pprint

@post('/')
def index(request):
	r = json.loads(request.body)
	if not r:
	    return "True"

	pprint.pprint(r)
	return "true"



if __name__ == "__main__": 

	run_itty(server='wsgiref', host='0.0.0.0', port=8080)