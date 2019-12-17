#!/usr/bin/env python 3
import sys, os.path
import webbrowser
import requests
import bs4 

DEBUG = True
html_file_name = 'catalogue.html'

res = None

def get_html_file(url):

	if not os.path.isfile(html_file_name):

		res = requests.get(url)
		res.raise_for_status()

		if DEBUG == True:
			html_file = open(html_file_name, 'wb')

			for chunk in res.iter_content(100000):
				html_file.write(chunk)

		html_file.close()

		#return res


def scrape_catalogue():

	if DEBUG == True:
		soup = bs4.BeautifulSoup(open(html_file_name), 'html.parser')
	else:
		soup = bs4.BeautifulSoup(res.text, 'html.parser')
	elems = soup.select('#RMS_afficherIris .ValorisationListeDesc a')
	print ("type elems: " + str(type(elems)))
	print ('type element 0: ' + str(type(elems[0])))
	
	#elems.find('.pRchrContent').extract()

	#Do not put 'prints' inside functions
	print ('nombre elements trouve: ' + str(len(elems)))

	#Put this outside of function
	for e in elems:
		print (e.getText())
		print ('\n')

if __name__ == "__main__":

	if DEBUG == True:
		search_text = 'Frank Zappa'
	else:
		if len(sys.argv) > 1:
			search_text = ''.join(sys.argv[1:])

	url = 'http://www.banq.qc.ca/techno/recherche/rms.html?q=' + search_text
	
	#uncomment the following line if you want to compare search results in browser
	#webbrowser.open(url)
	
	get_html_file(url)
	scrape_catalogue()


