#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web simple per obtenir nom de llibre de PACKT

@author: mrg20@alumnes.udl.cat
'''
import bs4
import urllib2

class Client():

	def htmlObtainer(self, page):
		#obtenir web
		f = urllib2.urlopen(page)
		htmlpage = f.read()
		f.close()
		return htmlpage


	def main(self):
		htmlpage = self.htmlObtainer("https://www.packtpub.com/packt/offers/free-learning/")
		#buscar dades
		lxmlpage = bs4.BeautifulSoup(htmlpage, 'lxml')
		parsed_lxml = lxmlpage.find("div", "dotd-title")
		book_title = parsed_lxml.find("h2").text
		print book_title
		#imprimir





if __name__ == '__main__':
	wc = Client()
	wc.main()