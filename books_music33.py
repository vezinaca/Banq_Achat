#!/usr/bin/env python3

from Utilitaires_BANQ import *
from Book_search_scrape import *

if __name__ == '__main__':
	#main()
	browser.quit()
	book_search_scrape = Book_search_scrape("http://333sound.com/33-13-series/", 's', "search_text", "#searchresults li")
	print ('allo')
	book_search_scrape.set_response(url)