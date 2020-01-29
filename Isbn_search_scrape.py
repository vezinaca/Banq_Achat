#!/usr/bin/env python3

from Utilitaires_BANQ import *
#from recaptcha import RecaptchaClient

#from lxml import html
from lxml import etree


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


	#all_books = post_process(open("isbnsearch_dungeon-dragon-art.html"), ".bookinfo")

	for book in my_books:
		another_soup = bs4.BeautifulSoup(book, 'html.parser')
		#h2 = another_soup.select("h2")
		#print(book)
		
		#print("===")
		#url =  "http://www.example.com/servlet/av/ResultTemplate=AVResult.html"
		#response = urlopen(url)
		#htmlparser = etree.HTMLParser()
		#tree = etree.parse(open("isbnsearch_dungeon-dragon-art.html"), htmlparser)
		#print(tree.xpath("p[1]"))
		#print(book.get_text())
		#title = book.find_element_by_xpath("h2")
		#page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
		
		#tree = html.fromstring(book.content)
		#This will create a list of buyers:
		#h2 = tree.xpath('h2')
		
		#print('H2: ', h2)
		
		#book.p

	#print (type(all_books))

	#print(all_books[0].get('.bookinfo h2'))
	#print(all_books[0].attrs)




	