#!/usr/bin/env python3

from Utilitaires_BANQ import *

from selenium.webdriver.support.ui import Select

formulaire_link = "https://www.banq.qc.ca/formulaires/suggestions_achat/index.html"

if __name__ == '__main__':
	
	creds = getCredentials()

	connect_to_site(browser, url, creds)

	browser.get(formulaire_link)

	time.sleep(5)

	title = browser.find_element_by_id('P5_TITRE')
	#title.send_keys("He-Man and the Masters of the Universe Omnibus")

	# select by visible text
	#select.select_by_visible_text('Banana')
	select_support = Select(browser.find_element_by_id('P5_SUPPORT'))
	select_support.select_by_value('Livre')

	select_recherche_iris = Select(browser.find_element_by_id('P5_RECHERCHE_IRIS'))
	select_recherche_iris.select_by_value('1')
	
	select_clientele = Select(browser.find_element_by_id('P5_CLIENTELE'))
	select_clientele.select_by_value('Adulte')

	commentaires = browser.find_element_by_id('P5_COMMENTAIRES')
	commentaires.send_keys('https://www.amazon.ca/He-Man-Masters-Universe-Omnibus-Robinson/dp/1401290493/ref=sr_1_4?keywords=heman&qid=1579199340&s=books&sr=1-4')
	
	'''
	<div class="BlocBouton">
      <input class="Bouton ButSubmit" value="Envoyer" type="submit">
    </div>
    '''
	#<input class="Bouton ButSubmit" value="Envoyer" type="submit">
	
	submit_button = browser.find_element_by_class_name('ButSubmit')
	submit_button.click()

	'''
	<textarea name="p_t03" rows="2" cols="45" id="P5_TITRE" class="banq_formFieldLarge"></textarea>

	<input type="text" id="P5_AUTEUR" name="p_t04" value="" size="60" maxlength="2000" class="banq_formFieldLarge">

	<input type="text" id="P5_EDITEUR" name="p_t05" value="" size="60" maxlength="2000" class="banq_formFieldLarge">

	<input type="text" id="P5_COLLECTION" name="p_t06" value="" size="60" maxlength="2000" class="banq_formFieldLarge">

	<input type="text" id="P5_DATE_EDITION" name="p_t07" value="" size="60" maxlength="4" class="banq_formFieldLarge">

	<textarea name="p_t08" rows="2" cols="45" id="P5_SUJET" class="banq_formFieldLarge"></textarea>
	
	<select name="p_t09" id="P5_SUPPORT" size="1" style="width:210px">
          <option value="" selected="selected"> </option>
          <option value="Livre">Livre</option>
          <option value="Livre numérique">Livre numérique</option>
          <option value="Musique (CD)">Musique (CD)</option>
          <option value="Film (DVD)">Film (DVD)</option>
          <option value="Film (Blu-ray)">Film (Blu-ray)</option>
          <option value="Livre sonore">Livre sonore</option>
          <option value="Livre sonore numérique">Livre sonore numérique</option>
          <option value="Jeu vidéo (PS3)">Jeu vidéo (PS3)</option>
          <option value="Jeu vidéo (PS4)">Jeu vidéo (PS4)</option>
          <option value="Jeu vidéo (Wii)">Jeu vidéo (Wii)</option>
          <option value="Jeu vidéo (Wii U)">Jeu vidéo (Wii U)</option>
          <option value="Jeu vidéo (Xbox 360)">Jeu vidéo (Xbox 360)</option>
          <option value="Jeu vidéo (Xbox One)">Jeu vidéo (Xbox One)</option>
          <option value="Document adapté (Braille, etc.)">Document adapté (braille, etc.)</option>
          <option value="Autre">Autre</option>
        </select>


      <select name="p_t10" id="P5_RECHERCHE_IRIS" size="1" style="width:60px">
          <option value="" selected="selected"></option>
          <option value="1">Oui</option>
          <option value="0">Non</option>
        </select>

        <select name="p_t11" id="P5_CLIENTELE" size="1" style="width:175px">
          <option value="" selected="selected"> </option>
          <option value="Adulte">Adulte</option>
          <option value="Jeune">Jeune (13 ans et moins)</option>
        </select>

        <textarea name="p_t12" rows="5" cols="45" id="P5_COMMENTAIRES" class="banq_formFieldLarge" wrap="virtual"></textarea>

'''