from Utilitaires_BANQ import *

print('allo')

if __name__ == '__main__':

	#url = 'http://banq.qc.ca/mon_dossier/mon_dossier.html'
	#browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/gecko/geckodriver")

	connect_to_site(browser, url)
	is_html_element_present_click(browser, 'Consulter mon dossier' , By.LINK_TEXT)
	time.sleep(4)
	is_html_element_present_click(browser, "//*[contains(text(), 'Borrowing history') or contains(text(), 'Historique des emprunts')]", By.XPATH)

	#infinite_scroll()
	time.sleep(4)
	