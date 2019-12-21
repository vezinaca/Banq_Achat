#!/usr/bin/env python 3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

mon_dossier_link = "http://banq.qc.ca/mon_dossier/mon_dossier.html"
loans_link = "https://cap.banq.qc.ca/account/loans"
reservations_link = "https://cap.banq.qc.ca/account/reservations"

browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/gecko/geckodriver")
# type (browser)


#browser.get('http://banq.qc.ca')
browser.get('http://banq.qc.ca/mon_dossier/mon_dossier.html')
#linkElem = browser.find_element_by_class_name('userOff')
#type(linkElem)
#linkElem.click()

#<a href="/accueil/index.html?language_id=1" xml:lang="en" lang="en">English</a>
#<a href="/accueil/index.html?language_id=3" lang="fr" xml:lang="fr">Français</a>



num_client = browser.find_element_by_id('NUM')
num_client.send_keys('00115446')
pwd = browser.find_element_by_id('PWD')
pwd.send_keys('19771314')
#pwd.submit()

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

#time.sleep(5)
#browser.navigate().to(loans_link)
#browser.GoTo(loans_link)


#Il faudrait s'assurer que le site demeure en français.  (une fois rendu ici, il switch en anglais)
#Par contre, je ne trouve pas le lien (a href) lorsque j'inspecte en utilisant les dev tools de Google Chrome???

'''
Ensuite, j'aimerais aller dans la section des emprunts mais encore une fois, je ne trouve pas de lien avec les dev tools?
Ce n'est qu'une fois avoir cliqué sur le 'lien' que je trouve le href dans la barre d'adresse ("https://cap.banq.qc.ca/account/loans")
Cependant, je vois ceci comme <div>. 

<div>
<!-- react-text: 976 -->
Borrowed and renewed items
<!-- react-text: 976 -->
</div>

'''
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
all_renew_buttons = browser.find_elements_by_xpath("//div[@class='cardActions_1423utz']/button[1]")
all_renew_buttons_text = browser.find_elements_by_xpath("//div[@class='cardActions_1423utz']/button[1]/div[1]/span[1]")
all_just_words_due_dates = browser.find_elements_by_xpath("//div[contains(text(),'Due date')]")
all_due_dates = browser.find_elements_by_xpath("//div[contains(text(),'Due date')]/preceding-sibling::div[1]")

print(len(all_renew_buttons))
#print(len(this_div))
##print(type(this_div))
#print(this_div.text)

for button_text in all_renew_buttons_text:
	print(button_text.text)
	print('\n')

for due_date in all_due_dates:
	print(due_date.text)
	print('\n')

for due_date_word in all_just_words_due_dates:
	print(due_date_word.text)
	print('\n')

#dict(zip(list1, zip(list2, list3)))
gros_dic = dict(zip(all_due_dates,zip(all_renew_buttons_text,all_renew_buttons)))

print('\n allo \n')
for k,v in gros_dic.items():
	print(k.text)
	le_text, piton = v
	print(le_text.text)
	print('\n')
#driver.find_element_by_xpath("//div[@class

#time.sleep(10)
#e = browser.find_elements_by_xpath("//*[contains(text(), 'Due date')]")
#print(len(e))
