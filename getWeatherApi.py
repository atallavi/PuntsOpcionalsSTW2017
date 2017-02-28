#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Get prevision from Weather Underground and give recomendations.


@author: Marc Ribalta Gene--mrg20@alumnes.udl.cat
'''

import sys
import requests #should download it


api_key = None #Should not do this

class WundergroundClient(object):

	urlbase = "http://api.wunderground.com/api/"
	url_services = {
		"hourly":"/hourly/q/CA/"
	}


	def __init__(self, apikey):
		self.apikey = apikey


	def hourly(self, location):
		#Get web info
		resp_format = "json"
		url = WundergroundClient.urlbase + self.apikey + \
			  WundergroundClient.url_services["hourly"] + \
			  location + "." + resp_format

		r = requests.get(url)

		print r.text
		#Parse info
		#Print Prevision
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