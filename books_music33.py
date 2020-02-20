#!/usr/bin/env python3

from Utilitaires_BANQ import *
from Book_search_scrape import *

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString

def insert_into_db(cnx, mycursor, valeurs):
	sql = "INSERT INTO thirtythreebooks (id, title, author) VALUES (%s, %s, %s)"
	mycursor.execute(sql, valeurs)
	cnx.commit()
	print(mycursor.rowcount, "record inserted.")

def delete_all_table_rows(cursor, table):
	cursor.execute("TRUNCATE TABLE " + table)
	cnx.commit()
	print ("Table " + table + " Truncated: %d rows deleted" % cursor.rowcount)


if __name__ == '__main__':
	#main()
	browser.quit()
	book_search_scrape_33 = Book_search_scrape("http://333sound.com/33-13-series/", 's', "search_text", "tr")
	#print (book_search_scrape_33.pre_url_search)
	#book_search_scrape_33.set_response(book_search_scrape_33.pre_url_search)

	cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='banq')
	my_cursor = cnx.cursor()

	delete_all_table_rows(my_cursor, 'thirtythreebooks')
	#exit()

	#book_search_scrape_33.create_local_html_file("333sound.html", book_search_scrape_33.response)
	my_search_results_33 = book_search_scrape_33.post_process(open("333sound.html"))
	my_path = 'images/33sound'

	nb_titre = 0
	nb_id = 0
	nb_auteur = 0

	for search_result in my_search_results_33:
		#print('in search results')
		
		all_td = search_result.select('td')
		#img = search_result.select_one('td > figure > img')
		#print(img['src'])
		#titre = search_result.select_one('.bookinfo > h2 > a').getText()
		#auteur = ' '.join(all_td[1].getText().split()[1:])
		#titre = all_td[1].select_one('i')


		#re.sub("[^0-9]", "", "sdkjh987978asd098as0980a98sd")

		le_html = str(all_td[1])
		#le_html_image = str(all_td[0])
		#print("html: " + le_html)
		#id_regex = re.compile(r'\d{3}')

		regex_id = re.compile(r'\d+')
		#mo = regex_id.search(le_html)
		#print(mo.group())



		#my_id = re.search('<td>(.*)\. ', le_html)
		mo_id = regex_id.search(le_html)
		if mo_id != None:
			my_id = mo_id.group()

		#substring = le_html[0:10]
		#my_id_85_from_sub = re.findall('[0-9]+', substring)
		#my_id = ' '.join(map(str, my_id_85_from_sub))

		#titre = re.search('\. (.*)</i>', le_html)
		titre = re.search('\.(.*)</i>', le_html)
		if titre != None:
			titre_sans_tag = replaceMultiple(titre.group(1), ["<i>"], "")
			


		#Prince’s Sign “☮” the Times
		auteur = re.search('<br/>by (.*)<br/>Buy', le_html)
		print("type(auteur....): ")
		print(type(auteur))
		#titre = re.search('<td>(.*)\. ', le_html)
		print('======')
		if my_id !=None:
			#print("id:_" + my_id.group(1))
			#this_id = re.sub("[^0-9]", "", my_id.group(1))
			print("id:_" + my_id)
			nb_id = nb_id + 1
		if titre != None:
			#print("titre:_" + titre.group(1))
			print("titre:_" + titre_sans_tag)
			nb_titre = nb_titre + 1
		if auteur != None:
			print("auteur:_" + auteur.group(1))
			nb_auteur = nb_auteur + 1

		#if (my_id == '10'):
		#	titre_sans_tag = "Prince’s Sign the Times"
		#titre_sans_tag = 'Prince’s Sign “☮” the Times'
		titre_sans_tag_remove_symbol = titre_sans_tag.replace(u"\u262E", '_')
		print(titre_sans_tag)

		print("TITRE SANS TAG: " + titre_sans_tag)
		if (auteur == None):
			my_author = 'Skip author'
		else:
			my_author = str(auteur.group(1))
		val = [str(my_id), str(titre_sans_tag_remove_symbol), my_author]
		insert_into_db(cnx, my_cursor, val)
		
		#titre = re.search('asdf=5;(.*)123jasd', le_html)
		#s = 'asdf=5;iwantthis123jasd'
		#result = re.search('asdf=5;(.*)123jasd', s)
		#print(result.group(1))

		#print(str(le_html))
		print("======")
		#exit()

		#auteur = all_td[1]

		#image_url = search_result.select_one('.image > a > img')
		#img_attribute = image_url['src']
		#fullfilename = os.path.join(my_path, book_search_scrape_isbn.replaceMultiple(titre, ['\\', '/', ' ', ','] , "_") + ".jpg")
		
		#print(title)
		#print("Titre: " + titre.text)
		#print("Auteur: " + str(auteur))
		'''
		print(recherche_isbn13)
		print(img_attribute)
		print(fullfilename)
		

		try:
			urllib.request.urlretrieve(img_attribute, fullfilename)
		except FileNotFoundError:
			"can't find file"
		photoBinaryData = book_search_scrape_isbn.convertToBinaryData(fullfilename)

		book_search_scrape_isbn.list_of_dic_books.append({'Titre':titre, 'Auteur': auteur, 'Recherche': recherche_isbn13, 'isbn_13': isbn_13, 'isbn_10': isbn_10, 'fullfilename': fullfilename})
		
		val = [str(titre), str(auteur), str("Printed Books"), str(recherche_isbn13), str(fullfilename), photoBinaryData, datetime.now(), False, False, 0]
		book_search_scrape_isbn.insert_into_db(cnx, my_cursor, val)	
		
		'''
	#cnx.close()
	
	#book_search_scrape_isbn.print_dictionnary()

	print("nb_id: " + str(nb_id))
	print("nb_titre: " + str(nb_titre))
	print("nb_auteur: " + str(nb_auteur))