#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Client web simple per obtenir nom de llibre de PACKT

@author: mrg20@alumnes.udl.cat--Marc Ribalta Gene
'''
import bs4
import urllib2
import subprocess

class Client():

	#obtenir web
	def html_obtainer(self, page):
		f = urllib2.urlopen(page)
		htmlpage = f.read()
		f.close()
		return htmlpage


	#buscar dades
	def search_data(self, htmlpage):
		lxmlpage = bs4.BeautifulSoup(htmlpage, 'lxml')
		parsed_lxml = lxmlpage.find("div", "dotd-title")
		book_title = parsed_lxml.find("h2").text
		return book_title


	#Print data
	def sendmessage(self, message):
		#If error on execute, install or reinstall  libnotify-bin
		subprocess.Popen(['notify-send', message])


	def main(self):
		htmlpage = self.html_obtainer("https://www.packtpub.com/packt/offers/free-learning/")
		book_title = self.search_data(htmlpage)
		self.sendmessage(book_title)



if __name__ == '__main__':
	wc = Client()
	wc.main()