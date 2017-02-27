#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web simple per obtenir nom de llibre de PACKT

@author: mrg20@alumnes.udl.cat
'''

import urllib2

class Client():
	page = "https://www.packtpub.com/packt/offers/free-learning/"

	def main(self):
		#obtenir web
		f = urllib2.urlopen(Client.page)
		htmlpage = f.read()
		f.close()
		print htmlpage
		#buscar dades
		#imprimir





if __name__ == '__main__':
	wc = Client()
	wc.main()