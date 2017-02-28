#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Get prevision from Weather Underground and give recomendations.


@author: Marc Ribalta Gene--mrg20@alumnes.udl.cat
'''

import sys


api_key = None #Should not do this

class WundergroundClient(object):


	def __init__(self, apikey):
		self.apikey = apikey


	def hourly(self, location):
		#Get web info
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