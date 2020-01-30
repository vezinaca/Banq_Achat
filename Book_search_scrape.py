#!/usr/bin/env python3

from Utilitaires_BANQ import *
#from recaptcha import RecaptchaClient

import os.path
import webbrowser
import requests
import bs4 


class Book_search_scrape(object):

	def __init__(self, pre_url_search, param_search, search_text, css_selector_media ):
		self.response = None
		self.list_of_dic_books = []
		self.pre_url_search = pre_url_search
		self.param_search = param_search
		self.search_text = search_text
		self.param_search_dic = {self.param_search: self.search_text}
		self.css_selector_media = css_selector_media
		
		
	def set_response(self, headers):
		self.response = requests.get(self.pre_url_search, params=self.param_search_dic, headers=headers)
		self.response.raise_for_status()
		#return res

	def create_local_html_file(self, html_file_name, response):
		
		if not os.path.isfile(html_file_name):
			html_file = open(html_file_name, 'wb')
			for chunk in response.iter_content(100000):
				html_file.write(chunk)

			html_file.close()

	def post_process(self, html):

		soup = bs4.BeautifulSoup(html, 'html.parser')
		my_links = soup.select(self.css_selector_media)
		return my_links

	def print_dictionnary(self):
		for media in self.list_of_dic_books:
			#python2
			#for k, v in d.iteritems():
			#	print k, v
			for k, v in media.items():
				print(k, v)
			print('\n')


if __name__ == '__main__':

	browser.quit()
	assert len(sys.argv) > 1, "Missing arguments."
	search_text = ' '.join(sys.argv[1:])

	book_search_scrape_isbn = Book_search_scrape("https://isbnsearch.org/search", 's', search_text, ".bookinfo")

	# from beautifulSoupPdf.py
	#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
	
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}

	#book_search_scrape.set_response(headers)

	#book_search_scrape.create_local_html_file("isbnsearch_kerouac.html", book_search_scrape.response)
	
	my_books_isbn = book_search_scrape_isbn.post_process(open("isbnsearch_kerouac.html"))

	for book in my_books_isbn:
		titre = book.find('a').getText()
		all_p = book.find_all('p')
		auteur = ' '.join(all_p[0].getText().split()[1:])
		recherche_isbn13 = ' '.join(all_p[1].getText().split()[1:])
		isbn_13 =all_p[1].getText()
		isbn_10 =all_p[2].getText()
		book_search_scrape_isbn.list_of_dic_books.append({'Titre':titre, 'Auteur': auteur, 'Recherche': recherche_isbn13, 'isbn_13': isbn_13, 'isbn_10': isbn_10})

	book_search_scrape_isbn.print_dictionnary()

	isbn_du_livre_recherche = book_search_scrape_isbn.list_of_dic_books[2].get('Recherche')
	print(isbn_du_livre_recherche)

	book_search_scrape_banq = Book_search_scrape("http://www.banq.qc.ca/techno/recherche/rms.html", 'q', isbn_du_livre_recherche, '#RMS_afficherIris .ValorisationListeDesc a')
	book_search_scrape_banq.set_response(headers)
	my_books_banq = book_search_scrape_banq.post_process(book_search_scrape_banq.response.text)

	book_search_scrape_banq.print_dictionnary()

	# if dic of banq is empty then remplir formulaire
	# insert infos in database personnal (that will eventually be online)
	# add program to veryfiy 4 times a week if book was found.
	# if book is found reserve it.  say something about bientot disponible.

	# s'inscrire a mon site pour gerer vos suggestions d'achats..
	#gerer les suggestions d'achats des gens...vous devez etre connecter dans une autre fenetre pour éviter la vie privée.  






	