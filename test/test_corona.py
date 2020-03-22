#!/usr/bin/env python3



from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time
import sys
import re
import os

url = 'http://banq.qc.ca/mon_dossier/mon_dossier.html?language_id=1'

def connect_to_site(browser, url, creds):
	browser.get(url)
	num_client = browser.find_element_by_id('NUM')
	num_client.send_keys(creds[0])
	pwd = browser.find_element_by_id('PWD')
	pwd.send_keys(creds[1])
	connection_button = browser.find_element_by_name('_eventId_proceed')
	connection_button.click()

def is_html_element_present_click(browser, link_text, by_search):
	delay = 3 # seconds
	link_verify = WebDriverWait(browser, delay).until(EC.presence_of_element_located((by_search, link_text)))
	print(link_text + " page is ready")
	print(link_verify)
	time.sleep(5)
	link_verify.click()

def main():
	print('connecting to site')
	
	browser = webdriver.Firefox(executable_path="/home/alienmint/Documents/Programmation/pythonPDF/Banq_Achat/gecko/geckodriver")

	creds = ('00115446', '19771314')

	connect_to_site(browser, url, creds)

	#is_html_element_present_click(browser, 'niveau2', By.CLASS_NAME)

	#def is_html_element_present_click(browser, link_text, by_search):
	#is_html_element_present_click(browser, 'niveau2', By.CLASS_NAME)
	
	delay = 3 # seconds
	message_important = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'MessageImportant')))
	close_covid = WebDriverWait(message_important, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'niveau2')))
	close_covid.click()

if __name__ == '__main__':
	main()