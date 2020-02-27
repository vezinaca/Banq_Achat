#!/usr/bin/env python3

import re

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString


if __name__ == '__main__':

	str_html_working = "<td>142. The Wild Tchoupitoulas’ <em>The Wild Tchoupitoulas</em><br/>by Bryan Wagner"
	str_html_not_working = "<td>85. Portishead’s <i>Dummy</i><br/>by RJ Wheaton<br/>Buy from Bloomsbury: <a href=66666"
	
	le_html = '<td>243. Dusty Springfield’s <i>Dusty in Memphis</i><br/>by Warren Zanes<br/>Buy from Bloomsbury: <a href="http://bloomsbury.com/us/dusty-springfields-dusty-in-memphis-9780826414922/">US</a> | <a href="http://bloomsbury.com/uk/dusty-springfields-dusty-in-memphis-9780826414922/">UK/Europe</a><br/><a href="http://www.amazon.com/Dusty-Springfields-Memphis-Thirty-Three/dp/0826414923/ref=sr_1_1?ie=UTF8&amp;qid=1391619650&amp;sr=8-1&amp;keywords=33+1%2F3+Dusty+in+Memphis">Amazon</a></td>'

	#<td>88. They Might Be Giants’ <i>Flood</i><br/>by S. Alexander Reed and Philip Sandifer<br/>Buy from Bloomsbury: <a href="http://bloomsbury.com/us/they-might-be-giants-flood-9781623569150/">US</a> | <a href="http://bloomsbury.com/uk/they-might-be-giants-flood-9781623569150/">UK/Europe</a><br/><a href="http://www.amazon.com/They-Might-Be-Giants-Flood/dp/162356915X/ref=sr_1_1?ie=UTF8&amp;qid=1391621140&amp;sr=8-1&amp;keywords=33+1%2F3+Flood">Amazon</a></td>
	html_andrew_wk = '<td>89. Andrew W.K.’s <em>I Get Wet</em><br/>by Phillip Crandall<br/>Buy from Bloomsbury: <a href="http://bloomsbury.com/us/andrew-wks-i-get-wet-9781623567149/">US</a> | <a href="http://bloomsbury.com/uk/andrew-wks-i-get-wet-9781623567149/">UK/Europe</a><br/><a href="http://www.amazon.com/Andrew-W-K-s-Get-Wet-33/dp/1623567149/ref=sr_1_1?ie=UTF8&amp;qid=1391621158&amp;sr=8-1&amp;keywords=33+1%2F3+I+Get+Wet">Amazon</a></td>'

	html_aphex_twin = '<td>90. Aphex Twin’s<em> Selected Ambient Works Volume II</em><em><br/></em>by Marc Weidenbaum<br/>Buy from Bloomsbury: <a href="http://bloomsbury.com/us/aphex-twins-selected-ambient-works-volume-ii-9781623568900/">US</a> | <a href="http://bloomsbury.com/uk/aphex-twins-selected-ambient-works-volume-ii-9781623568900/">UK/Europe</a><br/><a href="http://www.amazon.com/Aphex-Twins-Selected-Ambient-Volume/dp/1623568900/ref=sr_1_1?ie=UTF8&amp;qid=1386084799&amp;sr=8-1&amp;keywords=Aphex+Twin%27s+Selected+Ambient+Works+Volume+II" rel="noopener noreferrer" target="_blank" title="Amazon"> Amazon</a></td>'

	regex_id = re.compile(r'\d+')
	mo_id = regex_id.search(html_andrew_wk)
	print(mo_id.group())
	
	regex_titre = re.compile(r'\.(.*)(</i>|</em>)')
	regex_titre_old = re.compile(r'\.(.*)</i>')
	mo_titre = regex_titre.search(html_andrew_wk)
	mo_titre_old = regex_titre_old.search(html_andrew_wk)
	print(mo_titre.group())
	#print(mo_titre_old.group())

	print(replaceMultiple(mo_titre.group(), ["<em>", "</em>", "."], ''))

	regex_auteur = re.compile(r'(<br/>|</em>)by (.*)<br/>Buy')
	mo_auteur = regex_auteur.search(html_andrew_wk)
	if mo_auteur != None:
		print(mo_auteur.group())
		my_author = replaceMultiple(str(mo_auteur.group()), ["<i>", "<em>", "</em>", "<br/>", "Buy"], "")
		print("my author: " + my_author)
	else:
		print("no match auteur")
	

	'''
	titre = re.search('\.(.*)</i>', html_andrew_wk)
	if titre != None:
		titre_sans_tag = replaceMultiple(titre.group(1), ["<i>"], "")
	print(titre)
	'''
	#auteur = re.search('<br/>by (.*)<br/>Buy', le_html)
	