#!/usr/bin/env python3

from Utilitaires_BANQ import *

def renouvellement_livre():

	print("dans renouvellement_livre")
	
	#all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]/div[starts-with(@class,'cardStacked_')]")
	
	for card in all_cards_stacked:
		
		#title = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")
		title = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")		
		
		#borrowing_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/div[1]")
		#borrowing_date = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/div[1]")		
		borrowing_date = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[2]/div[starts-with(@class,'listContent_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[1]/div[1]")				
		
		#due_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[2]/div[1]/div[1]")
		#due_date = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[2]/div[1]/div[1]")		
		due_date = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[2]/div[starts-with(@class,'listContent_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[2]/div[1]/div[1]")				
		
		#renew_button_text = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[2]/div[@class='cardActions_1423utz']/button[1]/div[1]/span[1]")				

		#renew_button = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[2]/div[@class='cardActions_1423utz']/button[1]")				
		#renew_button = card.find_element_by_xpath("div[2]/div[@class='cardActions_1423utz']/button[1]")		
		renew_button = card.find_element_by_xpath("div[2]/div[starts-with(@class,'cardActions_')]/button[1]")		

		if(renew_button.text == "RENEW"):
			due_date_object = datetime.strptime(due_date.text, '%m/%d/%Y')

			difference_date = (due_date_object - today).days
			#print(str(difference_date))
			#print(difference_date < 16)
			if(difference_date < 5):
				#if "fury" in title.text or "free" in title.text:
				#	if "fury" in title.text:
				#		print('renew fury')
				#	if "free" in title.text:
				#		print('renew free')
				
				print("renew: " + str(title.text))		
				#renew_button.click()
				infinite_scroll()
				infinite_scroll()
				break
				
		
if __name__ == "__main__":

	browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/Banq_Achat/gecko/geckodriver")
	#browser = webdriver.Chrome(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/Banq_Achat/gecko/chromedriver")
	#when using Toshiba laptop
	#browser = webdriver.Firefox(executable_path="/home/labby/Documents/Programmation/pythonPDF/Banq_Achat/gecko/geckodriver")
	#browser = webdriver.Chrome(executable_path="/home/labby/Documents/Programmation/pythonPDF/Banq_Achat/gecko/chromedriver")
	
	creds = getCredentials()

	today = datetime.now()
	#remove message important because of Coronavirus
	time.sleep(2)

	#By.CLASS_NAME

	#niveau_2 = browser.find_element_by_class_name('niveau2')
	is_html_element_present_click(browser, 'niveau2', By.CLASS_NAME)
	#message_important = browser.find_element_by_id('MessageImportant')
	#niveau_2 = browser.find_element_by_class('niveau2')

	#message_important.click()
	exit()
	#remove message important because of Coronovirus
	#is_html_element_present_click(browser, "MessageImportant", By.ID)
	#is_html_element_present_click(browser, 'Consulter mon dossier' , By.LINK_TEXT)
	
	is_html_element_present_click(browser, "subscriber's account" , By.LINK_TEXT)
	#is_html_element_present_click(browser, "//*[contains(text(), 'subscriber\'s account') or contains(text(), 'Consulter mon dossier')]", By.XPATH)
	time.sleep(8)
	#is_html_element_present_click(browser, "//*[contains(text(), 'Borrowing history') or contains(text(), 'Historique des emprunts')]", By.XPATH)
	is_html_element_present_click(browser, "//*[contains(text(), 'Borrowed and renewed items')]", By.XPATH)
	
	time.sleep(4)
	#for this renouvellement page, i have to use infinite scroll twice.
	infinite_scroll()
	infinite_scroll()
			
	#//input[starts-with(@id, 'activation:') and contains(@id, ':voId:1')]
		
	first_card_stacked = browser.find_element_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")
	
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")
	print("size of all cards main: " + str(len(all_cards_stacked)))

	for i in range(len(all_cards_stacked)):
		renouvellement_livre()
		

	

	'''
			elif (renew_button.text == "NON-RENEWABLE"):
			all_non_renewable_buttons_to_click.append(renew_button)



	for button in all_non_renewable_buttons_to_click:
		print("click non renew!")
		#button.click()
		#time.sleep(3)
		#popup_button = browser.find_element_by_xpath("//body/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
		#print("click pop up non renew")
		#popup_button.click()


	'''



