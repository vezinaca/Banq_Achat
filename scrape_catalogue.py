#!/usr/bin/env python 3
import sys
import webbrowser
import requests
import bs4 

# Program line argument is used as search text.  If no pla is provided, 'Frank Zappa' is used as default.
if len(sys.argv) > 1:
	search_text = ''.join(sys.argv[1:])
else:
	search_text = 'Frank Zappa'

url = 'http://www.banq.qc.ca/techno/recherche/rms.html?q=' + search_text
#uncomment the following line if you want to compare search results in browser
webbrowser.open(url)
html_file_name = 'catalogue.html'

def get_html_file(url):

	req = requests.get(url)
	req.raise_for_status()

	html_file = open(html_file_name, 'wb')

	for chunk in req.iter_content(100000):
		html_file.write(chunk)

	html_file.close()

def scrape_catalogue():

	soup = bs4.BeautifulSoup(open(html_file_name), 'html.parser')
		
	elems = soup.select('#RMS_afficherIris .ValorisationListeDesc a')
	print ("type elems: " + str(type(elems)))
	print ('type element 0: ' + str(type(elems[0])))
	
	#elems.find('.pRchrContent').extract()

	#Do not put 'prints' inside functions
	print ('nombre elements trouve: ' + str(len(elems)))

	#Put this outside of function
	for e in elems:
		print(e.getText())
		print ('\n')

get_html_file(url)
scrape_catalogue()


