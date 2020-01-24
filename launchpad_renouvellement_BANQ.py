#!/usr/bin/env python3

from Utilitaires_BANQ import *

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")


lp = launchpad.Launchpad();
lp.Open()

def renew_book(renew_button):
	renew_button.click()
	infinite_scroll()
	infinite_scroll()

def get_all_status_books():
	pass

def illuminate_status_books(all_status_books):

	#[0, 7]
	#[16, 23]
	#[32, 39]

	all_cards_stacked = browser.find_elements_by_xpath("//div[starts-with(@class,'card_dzxwpk')]/div[starts-with(@class,'cardStacked_')]")

	button_number = 0

	for card in all_cards_stacked:
		title = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]")		
		borrowing_date = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[2]/div[starts-with(@class,'listContent_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[1]/div[1]/div[1]")				
		due_date = card.find_element_by_xpath("div[starts-with(@class,'cardContent_')]/div[2]/div[starts-with(@class,'listContent_')]/div[starts-with(@class,'cardContent_')]/div[1]/div[2]/div[1]/div[1]")				
		renew_button = card.find_element_by_xpath("div[2]/div[starts-with(@class,'cardActions_')]/button[1]")		

		if(renew_button.text == "RENEW"):
			due_date_object = datetime.strptime(due_date.text, '%m/%d/%Y')
			difference_date = (due_date_object - today).days
			if(difference_date < 100):
				lp.LedCtrlRaw(0, 0, 3)
				
				


				#infinite_scroll()
				#infinite_scroll()
				#break



def renouvellement_livre():

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
			if(difference_date < 100):
				if "fury" in title.text or "free" in title.text:
					if "fury" in title.text:
						print('renew fury')
					if "free" in title.text:
						print('renew free')
						
					#renew_button.click()
					infinite_scroll()
					infinite_scroll()
					break
				
		
if __name__ == "__main__":

	mode = "Mk1"
	# create an instance
	
	# Clear the buffer because the Launchpad remembers everything :-)
	lp.ButtonFlush()

	lp.LedAllOn()

	lp.Reset()

	but = lp.ButtonStateRaw()

	lp.LedCtrlRaw(22, 3, 3)
	lp.LedCtrlRaw(0, 3, 0)
	lp.LedCtrlXY(3,3,0,3)

	lp.ButtonFlush()

	lp.LedAllOn()

	lp.Reset()
		
	creds = getCredentials()

	today = datetime.now()
	connect_to_site(browser, url, creds)
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



