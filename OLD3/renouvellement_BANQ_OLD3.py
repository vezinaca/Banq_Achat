#!/usr/bin/env python3

from Utilitaires_BANQ import *

def renouvellement_livre():
	pass


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
		button.click()
		time.sleep(3)
		popup_button = browser.find_element_by_xpath("//body/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]")
		print("click pop up non renew")
		popup_button.click()



#pop up box
'''<div style="color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); transition: all 450ms cubic-bezier(0.23, 1, 0.32, 1) 0ms; box-sizing: border-box; font-family: Roboto; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 45px, rgba(0, 0, 0, 0.22) 0px 10px 18px; border-radius: 2px;"><h3 style="margin: 0px 0px -1px; padding: 24px 24px 20px; color: rgb(0, 0, 0); font-size: 22px; line-height: 32px; font-weight: 400; border-bottom: 1px solid rgb(136, 136, 136);">Non-renewable</h3><div style="font-size: 16px; color: rgba(0, 0, 0, 0.6); padding: 24px; box-sizing: border-box; overflow-y: auto; max-height: 122px;"><div><div style="color: rgb(0, 0, 0); display: block; font-size: 16px; line-height: 16px; position: relative; transition: all 450ms cubic-bezier(0.23, 1, 0.32, 1) 0ms; margin-left: 0px; padding: 16px 16px 16px 72px;"><svg viewBox="0 0 24 24" style="display: block; color: rgb(0, 0, 0); fill: rgb(244, 67, 54); height: 24px; width: 24px; user-select: none; transition: all 450ms cubic-bezier(0.23, 1, 0.32, 1) 0ms; position: absolute; top: 0px; margin: 12px; left: 4px;"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-2h2v2zm0-4h-2V7h2v6z"></path></svg><div>Transaction refused: renewal limit has been reached.</div></div></div></div><div style="box-sizing: border-box; padding: 8px; width: 100%; text-align: right; margin-top: -1px; border-top: 1px solid rgb(136, 136, 136);"><button tabindex="0" type="button" style="border: 10px none; box-sizing: border-box; display: inline-block; font-family: Roboto; cursor: pointer; text-decoration: none; margin: 0px; padding: 0px; outline: currentcolor none medium; font-size: inherit; font-weight: inherit; position: relative; height: 36px; line-height: 36px; min-width: 88px; color: rgb(66, 133, 244); transition: all 450ms cubic-bezier(0.23, 1, 0.32, 1) 0ms; border-radius: 2px; user-select: none; overflow: hidden; background-color: rgba(0, 0, 0, 0); text-align: center;"><div><span style="position: relative; padding-left: 16px; padding-right: 16px; vertical-align: middle; letter-spacing: 0px; text-transform: uppercase; font-weight: 500; font-size: 14px;">Close</span></div></button></div></div>'''


