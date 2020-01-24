#!/usr/bin/env python3

from Utilitaires_BANQ import *
#from recaptcha import RecaptchaClient


import os.path
import webbrowser
import requests
import bs4 


class Isbn_search_scrape(object):

	def __init__(self):
		self.test = 3
		
	def getTest(self):
		return self.test

	def __str__(self):
		pass

def get_response(parametres, headers):
	res = requests.get(pre_url_search, params=parametres, headers=headers)
	res.raise_for_status()
	return res
'''
def get_response(parametres):
	res = requests.get(pre_url_search, params=parametres)
	res.raise_for_status()
	return res
'''
def post_process(html, css_selector_media):

	soup = bs4.BeautifulSoup(html, 'html.parser')
	my_links = soup.select(css_selector_media)
	return my_links

if __name__ == '__main__':

	#recaptcha_client = RecaptchaClient('private key', 'public key')
	#data-sitekey="6Le3hh8TAAAAAODFPWK6yDdyyYGeE1YF71ymniO2"

	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}

	pre_url_search = "https://isbnsearch.org/search"
	search_text = "Frank Zappa"
	param_search = {'s': search_text}

	response = get_response(param_search, headers)
	
	#all_books = post_process(response.text, "body > div > div")
	all_books = post_process(response.text, ".bookinfo p")
	print (type(all_books))
	print(all_books)

	