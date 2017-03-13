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
	#Make a recomendation
	recomendation_degrees = {
	'calor':'Oportunity for a cold beer, wear short sleeve.',
	'normal':'Really good day, take a spring jacket.',
	'fred':'Cold, winter is comming.'
	}
	recomendation_sky = {
	'Clear' : ' Sunny day, come on go outside you antisocial.',
	'Mostly Clear' : ' Almost sunny, maybe you can go outside... Joking.',
	'Other' : ' You do not go outside when it is sunny, now even less.'
	}

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
		self.print_prevision("In an hour: ", jsoninfo[0])
		self.print_prevision("Next hours: ", jsoninfo[5])
		self.print_prevision("In 24 hours: ", jsoninfo[23])

		#Print recomendation
		parameter = jsoninfo[1]
		if (int(parameter["temp"]["metric"])>30):
			self.print_recomendation(parameter, "calor")
		elif ((int)(parameter["temp"]["metric"])<=30 and (int)(parameter["temp"]["metric"])>15):
			self.print_recomendation(parameter, "normal")
		else:
			self.print_recomendation(parameter, "fred")


	def print_prevision(self, phrase, parameter):
		print phrase
		print "    "+"The sky will be: "+parameter["wx"]
		print "    "+"Centigrate temperature: "+parameter["temp"]["metric"]
		print "    "+"The percentage of humidity will be: "+parameter["humidity"]


	def print_recomendation(self, parameter, degrees_esp):
		if(parameter["wx"]=="Clear" or parameter["wx"]=="Mostly Clear"):
			print WundergroundClient.recomendation_degrees[degrees_esp]+\
				WundergroundClient.recomendation_sky[parameter["wx"]]
		else:
			print WundergroundClient.recomendation_degrees[degrees_esp]+\
				WundergroundClient.recomendation_sky["Other"]


if __name__ == '__main__':

	if not api_key:
		try:
			api_key = sys.argv[1]
		except IndexError:
			print "Give me a key"



	wc = WundergroundClient(api_key)

	wc.hourly("Lleida")