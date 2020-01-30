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

def create_local_html_file(html_file_name, response):
	
	if not os.path.isfile(html_file_name):
		html_file = open(html_file_name, 'wb')
		for chunk in response.iter_content(100000):
			html_file.write(chunk)

		html_file.close()

def post_process(html, css_selector_media):

	soup = bs4.BeautifulSoup(html, 'html.parser')
	my_links = soup.select(css_selector_media)
	return my_links

def print_dictionnary(dic):
	for media in dic:
		#python2
		#for k, v in d.iteritems():
		#	print k, v
		for k, v in media.items():
			print(k, v)
		print('\n')

if __name__ == '__main__':

	#recaptcha_client = RecaptchaClient('private key', 'public key')
	#data-sitekey="6Le3hh8TAAAAAODFPWK6yDdyyYGeE1YF71ymniO2"

	# from beautifulSoupPdf.py
	#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'

	browser.quit()
	assert len(sys.argv) > 1, "Missing arguments."
	search_text = ' '.join(sys.argv[1:])
	
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}

	pre_url_search = "https://isbnsearch.org/search"
	#search_text = "Frank Zappa"
	param_search = {'s': search_text}

	#response = get_response(param_search, headers)

	#create_local_html_file("isbnsearch_dungeon-dragon-art.html", response)
	
	#titre, auteur, isbn

	soup = bs4.BeautifulSoup(open("isbnsearch_dungeon-dragon-art.html"), 'html.parser')
	my_books = soup.select(".bookinfo")

	list_of_dic_books = []
	#print(my_books[0].select('h2 a'))
	#all_books = post_process(open("isbnsearch_dungeon-dragon-art.html"), ".bookinfo")

	for book in my_books:
		#titre = book.select('h2 a').getText()
		titre = book.find('a').getText()
		all_p = book.find_all('p')
		#my_string.split()[:4] # first 4 words
		#search_text = ''.join(sys.argv[1:])
		#s2 = ' '.join(s.split()[1:])
		auteur = ' '.join(all_p[0].getText().split()[1:])
		recherche_isbn13 = ' '.join(all_p[1].getText().split()[1:])
		isbn_13 =all_p[1].getText()
		isbn_10 =all_p[2].getText()
		print(titre)
		print(auteur)
		print("recherche " + recherche_isbn13)
		print(isbn_10)
		print(isbn_13)
		print ("===")

		list_of_dic_books.append({'Titre':titre, 'Auteur': auteur, 'Recherche': recherche_isbn13, 'isbn_13': isbn_13, 'isbn_10': isbn_10})

	print_dictionnary(list_of_dic_books)

	




	