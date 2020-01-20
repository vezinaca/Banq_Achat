#!/usr/bin/env python3

#from Utilitaires_BANQ import *

import os.path
import webbrowser
import requests
import bs4 


DEBUG = True
#Currently not used
LOCAL = False
html_file_name = 'catalogue.html'



pre_url_search = 'http://www.banq.qc.ca/techno/recherche/rms.html?q='
pre_media_url = 'https://cap.banq.qc.ca'
css_selector_media = '#RMS_afficherIris .ValorisationListeDesc a'

#Currently not used
def create_local_html_file(html_file_name, response):
	
	if not os.path.isfile(html_file_name):
		html_file = open(html_file_name, 'wb')
		for chunk in response.iter_content(100000):
			html_file.write(chunk)

		html_file.close()


def get_response(url):
	res = requests.get(url)
	res.raise_for_status()
	return res

# This function takes a list of possible media links as argument and removes the non-media links
# returns dictionnary of media title as key and href of media as value.
def remove_non_media_links(list_links):
	
	only_media_list_of_dic = []

	for a_link in list_links:
		if not a_link['href'].startswith(pre_media_url):
			continue
		only_media_list_of_dic.append({'Title':a_link.getText(), 'Link':a_link['href'], 'future_key': 'future_value'})
		
	return only_media_list_of_dic

def post_process(html):

	soup = bs4.BeautifulSoup(html, 'html.parser')
	my_links = soup.select(css_selector_media)
	return(remove_non_media_links(my_links))

'''
def verify_presence_by_link_text_click(browser, link_text):
	delay = 3 # seconds
	try:
	    link_verify = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
	    print(link_text + " page is ready")
	    link_verify.click()
	except TimeoutException:
		print ("Loading of " + link_text + "took too much time!")

def verify_presence_by_xpath_click(browser, link_text):
	delay = 8 # seconds
	try:
	    link_verify = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, link_text)))
	    print(link_text + " page is ready")
	    link_verify.click()
	except TimeoutException:
		print ("Loading of " + link_text + "took too much time!")
'''
if __name__ == "__main__":

	#creds = getCredentials()

	#connect_to_site(browser, url, creds)

	if DEBUG == True:
		search_text = 'Frank Zappa'
	else:
		assert len(sys.argv) > 1, "Missing arguments."
		#if len(sys.argv) > 1:
		search_text = ''.join(sys.argv[1:])

	url = pre_url_search + search_text

	print (url)
	#uncomment the following line if you want to compare search results in browser
	#webbrowser.open(url)
	
	response = get_response(url)
	print(response.text)
	
	list_of_dic_of_medias = post_process(response.text)

	print(list_of_dic_of_medias)

	for media in list_of_dic_of_medias:
		#python2
		#for k, v in d.iteritems():
		#	print k, v
		for k, v in media.items():
			print(k, v)
		print('\n')
	
	
	#is_html_element_present_click(browser, "Forms", By.LINK_TEXT)

	#<a href="/formulaires/index.html">Formulaires</a>
	#verify_presence_by_link_text_click(browser, "Formulaires")
	#<a href="/formulaires/suggestions_achat/index.html">» Suggestions d'achat</a>

	#time.sleep(5)

	#<a href="/formulaires/suggestions_achat/index.html">» Purchase suggestion</a>
	#is_html_element_present_click(browser, " Purchase suggestion", By.LINK_TEXT)
	#is_html_element_present_click(browser, "//*[contains(text(), '» Purchase suggestion')", By.LINK_TEXT)
	
	#is_html_element_present_click(browser, " Purchase suggestion", By.LINK_TEXT)

	#verify_presence_by_link_text_click(browser, " Suggestions d'achat")