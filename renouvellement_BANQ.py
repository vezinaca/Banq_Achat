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
    print("page is ready")
except TimeoutException:
	print ("Loading took too much time!")


#WebDriverWait(browser, 10).until(lambda browser: EC.presence_of_element_located((By.LINK_TEXT, 'Consulter mon dossier')) != None)
consul_dossier = browser.find_element_by_link_text('Consulter mon dossier')
consul_dossier.click()


#Il faudrait s'assurer que le site demeure en français.  (une fois rendu ici, il switch en anglais)
#Par contre, je ne trouve pas le lien (a href) lorsque j'inspecte en utilisant les dev tools de Google Chrome???

'''
delay = 10 # seconds
try:
    link_borrowed_items = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.LINK_TEXT, 'Borrowed and renewed items')))
    print("page is ready")
    link_borrowed_items.click()
except TimeoutException:
	print ("Loading took too much time!")

'''

time.sleep(8)
e = browser.find_element_by_xpath("//*[contains(text(), 'Borrowed and renewed items')]")
e.click()

#parent DIV class = "cardContent_p5m42o"

#driver.find_element_by_xpath("//form[1]")
#email_input = driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")

time.sleep(8)
#driver.find_element_by_xpath("//div[contains(@class, 'first_name')]")
#driver.find_element_by_class_name("first_name")
#this_div = browser.find_element_by_xpath("//div[contains(@class,'cardContent_p5m42o')]")

'''
<div class="header">Planets</div>
<div class="event">Jupiter</div>
<div class="event">Mars</div>

<div class="header">Stars</div>
<div class="event">Acturus</div>
<div class="event">Pleaides</div>
'''
#all_renew_buttons = browser.find_elements_by_xpath("//div[@class='cardActions_1423utz']/button[1]/span[1]")
#driver.find_elements_by_xpath("//div[@class='event']/preceding-sibling::div[@class='header']")

# for book titles
#<div class="cardContent_p5m42o">

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

#dict(zip(list1, zip(list2, list3)))
gros_dic = dict(zip(all_due_dates,zip(all_renew_buttons_text,all_renew_buttons)))
#gros_dic = dict(zip(datetime.datetime.strptime(all_due_dates, '%d/%m/%Y'),zip(all_renew_buttons_text,all_renew_buttons)))

print('\n allo \n')
for k,v in gros_dic.items():
	print(k.text)
	le_text, piton = v
	print(le_text.text)
	print('\n')

date = "1/8/2022"

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

#driver.find_element_by_xpath("//div[@class

#time.sleep(10)
#e = browser.find_elements_by_xpath("//*[contains(text(), 'Due date')]")
#print(len(e))
