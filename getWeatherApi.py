#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Get prevision from Weather Underground and give recomendations.


@author: Marc Ribalta Gene--mrg20@alumnes.udl.cat
'''

import sys
import requests #should download it
import json

api_key = None #Should not even do this

class WundergroundClient(object):

	urlbase = "http://api.wunderground.com/api/"
	url_services = {
		"hourly":"/hourly/q/CA/"
	}


	def __init__(self, apikey):
		self.apikey = apikey


	#Get web info
	def get_web(self, location):
		resp_format = "json"
		url = WundergroundClient.urlbase + self.apikey + \
			  WundergroundClient.url_services["hourly"] + \
			  location + "." + resp_format

		r = requests.get(url)

		return r	


	def hourly(self, location):
		r = self.get_web(location)
		#Parse info
		jsondata = json.loads(r.text)
		jsoninfo = jsondata["hourly_forecast"]
		#Print Prevision
		print "Prevision for "+location
		print jsoninfo[0]["wx"]
		print jsoninfo[0]["humidity"]
		print jsoninfo[0]["temp"]["metric"]
		#Make a recomendation
		#Print recomendation





if __name__ == '__main__':

	if not api_key:
		try:
			api_key = sys.argv[1]
		except IndexError:
			print "Give me a key"



	wc = WundergroundClient(api_key)

	wc.hourly("Lleida")