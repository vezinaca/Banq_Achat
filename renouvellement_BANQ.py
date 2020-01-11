#!/usr/bin/env python3

from Utilitaires_BANQ import *



def renouvellement_livre():

	print("dans renouvellement_livre")
	
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")
	#print("size of all cards main: " + str(len(all_cards_stacked)))

	for card in all_cards_stacked:
		
		#author_name = author.find_element_by_xpath("div[@class='meta-values metaValue_tcono5']/span[1]")
		title = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")
		borrowing_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/div[1]")
		due_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[2]/div[1]/div[1]")
		#type_document_name = card.find_element_by_xpath("div[@class='meta-values metaValue_tcono5']/span[1]")
		#renew_button_text = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[2]/div[@class='cardActions_1423utz']/button[1]/div[1]/span[1]")				
		renew_button = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[2]/div[@class='cardActions_1423utz']/button[1]")				
		
		#if "Kerouac" not in str(title.text):
		#if "hacks" in str(title.text) or "AWS" in str(title.text):
		if(renew_button.text == "RENEW"):
			#print("oui hacks or aws")
			due_date_object = datetime.strptime(due_date.text, '%m/%d/%Y')

			difference_date = (due_date_object - today).days
			#print(str(difference_date))
			#print(difference_date < 16)
			if(difference_date < 100):
				if "free" in title.text:
					print('renew Then again')
					renew_button.click()
					infinite_scroll()
					infinite_scroll()
					break
				if "fury" in title.text:
					print('renew streak')
					renew_button.click()
					infinite_scroll()
					infinite_scroll()
					break

				if "Kerouac" in str(title.text):
					#print('kerouac oui')
					continue
				
		
if __name__ == "__main__":

	today = datetime.now()
	connect_to_site(browser, url)
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
	#scroll_to_bottom()
	#scroll_to_bottom()
	
		
	#//input[starts-with(@id, 'activation:') and contains(@id, ':voId:1')]
	#all_cards = browser.find_elements_by_xpath("//div[starts-with(@class, 'cardContent_')]") 
	
	
	first_card_stacked = browser.find_element_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")
	#print("first card stacked found " + first_card_stacked.text)
	renew_button = first_card_stacked.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[2]/div[@class='cardActions_1423utz']/button[1]")				
	#print("renew button text: " + renew_button.text)

	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")
	print("size of all cards main: " + str(len(all_cards_stacked)))

	for i in range(len(all_cards_stacked)):
		#print(str(i) + ')on passe dans la boucle')
		renouvellement_livre()
		#time.sleep(3)

	#print("nombre husker: " + str(nombre_husker))

	'''
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")
	print("size of all cards main: " + str(len(all_cards_stacked)))

	all_renew_buttons_to_click = []
	all_non_renewable_buttons_to_click = []
	for card in all_cards_stacked:
		
		title = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")
		borrowing_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/div[1]")
		due_date = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[@class='cardContent_p5m42o']/div[2]/div[@class='listContent_1nnce6d']/div[@class='cardContent_p5m42o']/div[1]/div[2]/div[1]/div[1]")
		
		#renew_button_text = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[2]/div[@class='cardActions_1423utz']/button[1]/div[1]/span[1]")				
		renew_button = card.find_element_by_xpath("div[@class='cardStacked_n7d4vb']/div[2]/div[@class='cardActions_1423utz']/button[1]")				
		
		print("====begin====")
		print(renew_button.text)
		print("====end====")


		if(renew_button.text == "RENEW"):

			due_date_object = datetime.strptime(due_date.text, '%m/%d/%Y')

			difference_date = (due_date_object - today).days
			print(str(difference_date))
			print(difference_date < 16)
			if(difference_date < 16):
				all_renew_buttons_to_click.append(renew_button)
				#renew_button.click()
		elif (renew_button.text == "NON-RENEWABLE"):
			all_non_renewable_buttons_to_click.append(renew_button)


		print(title.text)
		print(borrowing_date.text)
		print(due_date.text)

	for button in all_renew_buttons_to_click:
		print("click renew!")
		#button.click()

	for button in all_non_renewable_buttons_to_click:
		print("click non renew!")
		#button.click()
		#time.sleep(3)
		#popup_button = browser.find_element_by_xpath("//body/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
		#print("click pop up non renew")
		#popup_button.click()


	'''



