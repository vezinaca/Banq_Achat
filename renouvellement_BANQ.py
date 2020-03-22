#!/usr/bin/env python3

from Utilitaires_BANQ import *

def renouvellement_livre(browser):

	print("dans renouvellement_livre")
	
	
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]/div[starts-with(@class,'cardStacked_')]")
	
	for card in all_cards_stacked:
		
		title = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")		
		borrowing_date = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[2]/div[starts-with(@class,'listContent_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[1]/div[1]")				
		due_date = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[2]/div[starts-with(@class,'listContent_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[2]/div[1]/div[1]")				
		renew_button = card.find_element_by_xpath("div[2]/div[starts-with(@class,'cardActions_')]/button[1]")		

		if(renew_button.text == "RENEW"):
			due_date_object = datetime.strptime(due_date.text, '%m/%d/%Y')

			difference_date = (due_date_object - today).days
			#print(str(difference_date))
			#print(difference_date < 16)
			if(difference_date < 5):
				print("renew: " + str(title.text))		
				#renew_button.click()
				infinite_scroll(browser)
				infinite_scroll(browser)
				break
				
		
if __name__ == "__main__":

	browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/Banq_Achat/gecko/geckodriver")
	creds = getCredentials()
	connect_to_site(browser, url, creds)

	today = datetime.now()
	
	time.sleep(2)

	#remove message important because of Coronavirus
	kill_coronavirus_alert_message(browser)
	
	#is_html_element_present_click(browser, "subscriber's account" , By.LINK_TEXT)
	get_html_element(browser, "subscriber's account" , By.LINK_TEXT).click()
	time.sleep(8)
	#is_html_element_present_click(browser, "//*[contains(text(), 'Borrowed and renewed items')]", By.XPATH)
	get_html_element(browser, "//*[contains(text(), 'Borrowed and renewed items')]", By.XPATH).click()

	time.sleep(4)
	#for this renouvellement page, i have to use infinite scroll twice.
	infinite_scroll(browser)
	infinite_scroll(browser)
			
	#//input[starts-with(@id, 'activation:') and contains(@id, ':voId:1')]
		
	first_card_stacked = browser.find_element_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")
	
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")
	print("size of all cards main: " + str(len(all_cards_stacked)))

	for i in range(len(all_cards_stacked)):
		renouvellement_livre(browser)
			
		#Non renewable pop up management
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



