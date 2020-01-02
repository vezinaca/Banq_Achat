#!/usr/bin/env python 3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import datetime

mon_dossier_link = "http://banq.qc.ca/mon_dossier/mon_dossier.html"
loans_link = "https://cap.banq.qc.ca/account/loans"
reservations_link = "https://cap.banq.qc.ca/account/reservations"
browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/gecko/geckodriver")

browser.get('http://banq.qc.ca/mon_dossier/mon_dossier.html')
num_client = browser.find_element_by_id('NUM')
num_client.send_keys('00115446')
pwd = browser.find_element_by_id('PWD')
pwd.send_keys('19771314')

connection_button = browser.find_element_by_name('_eventId_proceed')
connection_button.click()

delay = 3 # seconds
try:
    link_consul_dossier = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Consulter mon dossier')))
    print("Consulter mon dossier page is ready")
except TimeoutException:
	print ("Loading took too much time!")


#WebDriverWait(browser, 10).until(lambda browser: EC.presence_of_element_located((By.LINK_TEXT, 'Consulter mon dossier')) != None)
consul_dossier = browser.find_element_by_link_text('Consulter mon dossier')
consul_dossier.click()


#Il faudrait s'assurer que le site demeure en français.  (une fois rendu ici, il switch en anglais)
#Par contre, je ne trouve pas le lien (a href) lorsque j'inspecte en utilisant les dev tools de Google Chrome???


delay = 8 # seconds
try:
    link_borrowed_items = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Borrowed and renewed items')]")))
    print("Borrowed page is ready")
    link_borrowed_items.click()
except TimeoutException:
	print ("Loading Borrowed page took too much time!")


#time.sleep(8)

##=================================================================
#infinite scroll
# https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

p = 1
try:
	#while True:
	for i in range(5):
	    # Scroll down to bottom
	    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	    # Wait to load page
	    time.sleep(SCROLL_PAUSE_TIME)
	    print(str(p) + ") " +'scrolling...')
	    p = p + 1

	    # Calculate new scroll height and compare with last scroll height
	    new_height = browser.execute_script("return document.body.scrollHeight")
	    if new_height == last_height:
	        break
	    last_height = new_height
except KeyboardInterrupt:
	print('allo')


'''

##================================================================
all_book_titles = browser.find_elements_by_xpath("//div[@class='cardContent_p5m42o']/div[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]") 
all_renew_buttons = browser.find_elements_by_xpath("//div[@class='cardActions_1423utz']/button[1]")
all_renew_buttons_text = browser.find_elements_by_xpath("//div[@class='cardActions_1423utz']/button[1]/div[1]/span[1]")
all_just_words_due_dates = browser.find_elements_by_xpath("//div[contains(text(),'Due date')]")
all_due_dates = browser.find_elements_by_xpath("//div[contains(text(),'Due date')]/preceding-sibling::div[1]")

print(len(all_renew_buttons))
#print(len(this_div))
##print(type(this_div))
#print(this_div.text)

for book_title in all_book_titles:
	print("titre: " + book_title.text)
	print('\n')
all_due_dates_datetime = []

for button_text in all_renew_buttons_text:
	print(button_text.text)
	print('\n')

for due_date in all_due_dates:
	print(due_date.text)
	all_due_dates_datetime.append(datetime.datetime.strptime(due_date.text, '%d/%m/%Y'))
	print('\n')

for due_date_word in all_just_words_due_dates:
	print(due_date_word.text)
	print('\n')

for due_date_datetime in all_due_dates_datetime:
	print(due_date_datetime)
	print('shit')

print("size of all_due_dates: " + str(len(all_due_dates)))
print("size of all_due_dates_datetime: " + str(len(all_due_dates_datetime)))

#dict(zip(list1, zip(list2, list3)))
#gros_dic = dict(zip(all_due_dates,zip(all_renew_buttons_text,all_renew_buttons)))
#gros_dic = dict(zip(datetime.datetime.strptime(all_due_dates, '%d/%m/%Y'),zip(all_renew_buttons_text,all_renew_buttons)))
gros_dic = dict(zip(all_due_dates_datetime,zip(all_renew_buttons_text,all_renew_buttons)))
print('\n ==================================================allo \n')
print("size of gros_dic: " + str(len(gros_dic)))
for k,v in gros_dic.items():
	#print(k.text)
	#print(type(k.text))
	print(k)
	print(type(k))
	le_text, piton = v
	print(le_text.text)
	print('\n')

date = "1/8/2022"
aujourdhui = datetime.datetime.now()

'''




'''
for k,v in gros_dic.items():
	if (k.text == date):
		print ("k.text == date oui")
		le_text, piton = v
		if (le_text.text == "RENEW"):
			print('on renouvelle')
			piton.click()
			exit()
	else:
		print('non pas de renouvellement')
'''