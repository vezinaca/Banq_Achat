#!/usr/bin/env python3

from Utilitaires_BANQ import *

if __name__ == "__main__":

	today = datetime.now()
	connect_to_site(browser, url)
	is_html_element_present_click(browser, 'Consulter mon dossier' , By.LINK_TEXT)
	time.sleep(8)
	#is_html_element_present_click(browser, "//*[contains(text(), 'Borrowing history') or contains(text(), 'Historique des emprunts')]", By.XPATH)
	is_html_element_present_click(browser, "//*[contains(text(), 'Borrowed and renewed items')]", By.XPATH)
	
	time.sleep(4)
	infinite_scroll()
	time.sleep(4)
	
	#//input[starts-with(@id, 'activation:') and contains(@id, ':voId:1')]
	#all_cards = browser.find_elements_by_xpath("//div[starts-with(@class, 'cardContent_')]") 
	
	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]")

	print("size of all cards main: " + str(len(all_cards_stacked)))

	all_renew_buttons_to_click = []
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


		print(title.text)
		print(borrowing_date.text)
		print(due_date.text)

	for button in all_renew_buttons_to_click:
		print("ca click!")
		#button.click()


