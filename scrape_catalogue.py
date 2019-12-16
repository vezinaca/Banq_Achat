#!/usr/bin/env python 3



# DISCUSSION ENTRE GREG ET CARL
# CARL - I am aware of the hard coded stuff in there.
# GREG - Well, if you are aware of it, why are you keeping it in there?

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

	#Would it be better if this function had a 'return'? i.e elementsTrouves = scrapeCatalogue()
	#Then I would iterate and print the elementsTrouves array?

get_html_file(url)
scrape_catalogue()


'''
I'm able to get all the <a> tags that are in '#RMS_afficherIris .ValorisationListeDesc a'. 
However as you can see, they are not all titles.  One of them in this case is a 
link to 'Acces par PRETNUMERIQUE.CA (format ePub)', which I don't want.  I guess it doesn't 
really matter, seeing as obviously this will never be a match with what I'm looking for.  I still
think it's better to get rid of it. 

To do so, I think I would need to 'extract' the <span class="pRchrContent"> from the document then go get
the <a> tags the same way I'm proceeding now.

I've tried a couple of things I saw in the documentation, but It doesn't seem to work.  

'''
