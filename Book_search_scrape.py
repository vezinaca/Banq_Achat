#!/usr/bin/env python3

from Utilitaires_BANQ import *
#from recaptcha import RecaptchaClient

import os.path
import webbrowser
import requests
import bs4 
import mysql.connector
import urllib.request


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

	def delete_all_table_rows(self, cursor, table):
		cursor.execute("TRUNCATE TABLE " + table)

	# For inserting file as blob in database
	def convertToBinaryData(self, filename):
	    # Convert digital data to binary format
	    with open(filename, 'rb') as file:
	        binaryData = file.read()
	    return binaryData

	#not used
	def write_file(self, data, filename):
	    # Convert binary data to proper format and write it on Hard Disk
	    with open(filename, 'wb') as file:
	        file.write(data)

	def insert_into_db(self, cnx, mycursor, valeurs):
		sql = "INSERT INTO commande (title, author, type_document, isbn, image_name, img, date_ordered, received, nb_emails_sent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		mycursor.execute(sql, valeurs)
		cnx.commit()
		print(mycursor.rowcount, "record inserted.")
		
	#Used to replace '/' and '\' that might appear in filename
	def replaceMultiple(self, mainString, toBeReplaces, newString):
	    # Iterate over the strings to be replaced
	    for elem in toBeReplaces :
	        # Check if string is in the main string
	        if elem in mainString :
	            # Replace the string
	            mainString = mainString.replace(elem, newString)
	    
	    return  mainString  


if __name__ == '__main__':

	cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='banq')
	my_cursor = cnx.cursor()
	#delete_all_table_rows(my_cursor, "commande")	

	browser.quit()
	assert len(sys.argv) > 1, "Missing arguments."
	search_text = ' '.join(sys.argv[1:])

	#book_search_scrape_isbn = Book_search_scrape("https://isbnsearch.org/search", 's', search_text, ".bookinfo")
	book_search_scrape_isbn = Book_search_scrape("https://isbnsearch.org/search", 's', search_text, "#searchresults li")
	# from beautifulSoupPdf.py
	#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
	
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}

	#book_search_scrape_isbn.set_response(headers)

	#book_search_scrape_isbn.create_local_html_file("hawking.html", book_search_scrape_isbn.response)
	
	#my_books_isbn = book_search_scrape_isbn.post_process(open("isbnsearch_kerouac.html"))

	#my_books_isbn = book_search_scrape_isbn.post_process(open("isbnsearch_hole.html"))
	
	#<img src="https://images-na.ssl-images-amazon.com/images/I/410iKQv9qjL._SL160_.jpg" alt="Hole's Live Through This (33 1/3)">
	'''
	for book in my_books_isbn:
		titre = book.find('a').getText()
		all_p = book.find_all('p')
		auteur = ' '.join(all_p[0].getText().split()[1:])
		recherche_isbn13 = ' '.join(all_p[1].getText().split()[1:])
		isbn_13 =all_p[1].getText()
		isbn_10 =all_p[2].getText()
		book_search_scrape_isbn.list_of_dic_books.append({'Titre':titre, 'Auteur': auteur, 'Recherche': recherche_isbn13, 'isbn_13': isbn_13, 'isbn_10': isbn_10})
	'''


	#my_search_results_isbn = book_search_scrape_isbn.post_process(open("isbnsearch_kerouac2.html"))
	#my_search_results_isbn = book_search_scrape_isbn.post_process(book_search_scrape_isbn.response.text)
	my_search_results_isbn = book_search_scrape_isbn.post_process(open("isbnsearch_hole.html"))
	my_path = 'images/commandes'

	for search_result in my_search_results_isbn:
		'''

		print(search_result)
		bookinfo = search_result.find('.image')
		bookinfo = search_result.select('.image')
		print("blah " + str(bookinfo))
		'''
		'''
		titre = search_result.find('.bookinfo > a').getText()
		all_p = search_result.find_all('.bookinfo > p')
		auteur = ' '.join(all_p[0].getText().split()[1:])
		recherche_isbn13 = ' '.join(all_p[1].getText().split()[1:])
		isbn_13 =all_p[1].getText()
		isbn_10 =all_p[2].getText()
		image_url = search_result.find('.image > img')
		img_attribute = image_url['src']
		fullfilename = os.path.join(my_path, book_search_scrape_isbn.replaceMultiple(titre, ['\\', '/', ' ', ','] , "_") + ".jpg")
		'''
		#title = search_result.find("h4", class_="h12 talk-link__speaker").text
		#title = search_result.find(class_="bookinfo", "h2", "a").text

		titre = search_result.select_one('.bookinfo > h2 > a').getText()
		all_p = search_result.select('.bookinfo > p')
		auteur = ' '.join(all_p[0].getText().split()[1:])
		recherche_isbn13 = ' '.join(all_p[1].getText().split()[1:])
		isbn_13 =all_p[1].getText()
		isbn_10 =all_p[2].getText()
		image_url = search_result.select_one('.image > a > img')
		img_attribute = image_url['src']
		fullfilename = os.path.join(my_path, book_search_scrape_isbn.replaceMultiple(titre, ['\\', '/', ' ', ','] , "_") + ".jpg")
		
		#print(title)
		print(titre)
		print(auteur)
		print(recherche_isbn13)
		print(img_attribute)
		print(fullfilename)
		

		try:
			urllib.request.urlretrieve(img_attribute, fullfilename)
		except FileNotFoundError:
			"can't find file"
		photoBinaryData = book_search_scrape_isbn.convertToBinaryData(fullfilename)

		book_search_scrape_isbn.list_of_dic_books.append({'Titre':titre, 'Auteur': auteur, 'Recherche': recherche_isbn13, 'isbn_13': isbn_13, 'isbn_10': isbn_10, 'fullfilename': fullfilename})
		
		val = [str(titre), str(auteur), str("Printed Books"), str(recherche_isbn13), str(fullfilename), photoBinaryData, datetime.now(), False, 0]
		book_search_scrape_isbn.insert_into_db(cnx, my_cursor, val)	

	cnx.close()
	exit()

	book_search_scrape_isbn.print_dictionnary()

	

	isbn_du_livre_recherche = book_search_scrape_isbn.list_of_dic_books[0].get('Recherche')
	print(isbn_du_livre_recherche)

	

	book_search_scrape_banq = Book_search_scrape("http://www.banq.qc.ca/techno/recherche/rms.html", 'q', isbn_du_livre_recherche, '#RMS_afficherIris .ValorisationListeDesc a')
	book_search_scrape_banq.set_response(headers)
	my_books_banq = book_search_scrape_banq.post_process(book_search_scrape_banq.response.text)

	book_search_scrape_banq.print_dictionnary()

	if (len(my_books_banq) == 0):
		print('The book ' + book_search_scrape_isbn.list_of_dic_books[0].get('Titre') + ' by ' + book_search_scrape_isbn.list_of_dic_books[0].get('Auteur') + ' was not found in the BANQ catalogue.')
		

	# if dic of banq is empty then remplir formulaire
	# insert infos in database personnal (that will eventually be online)
	# add program to veryfiy 4 times a week if book was found.
	# if book is found reserve it.  say something about bientot disponible.

		#fields to have in database table....recu ou non.  id, titre, auteur, isbn, date commande, recu

	# s'inscrire a mon site pour gerer vos suggestions d'achats..
	#gerer les suggestions d'achats des gens...vous devez etre connecter dans une autre fenetre pour éviter la vie privée.  






	