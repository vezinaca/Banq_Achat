#!/usr/bin/env python3

import re

if __name__ == '__main__':

	str_html_working = "<td>142. The Wild Tchoupitoulas’ <em>The Wild Tchoupitoulas</em><br/>by Bryan Wagner"
	str_html_not_working = "<td>85. Portishead’s <i>Dummy</i><br/>by RJ Wheaton<br/>Buy from Bloomsbury: <a href=66666"
	
	#my_id_85 = re.search('<td>(.*)\. ', str_html_not_working)
	 
	#my_id_85 = re.search('<td>([^0-9])<br/>', str_html_not_working)

	'''
	s = 'asdf=5;iwantthis123jasd'
	start = 'asdf=5;'
	end = '123jasd'
	'''
	
	'''
	start = '<td>'
	end = '<br/>'
	#result = re.search('%s[0-9]+%s' % (start, end), str_html_not_working).group(1)
	result = re.search('%s/d+%s' % (start, end), str_html_not_working).group(1)
	print(result)

	exit()
	'''

	'''
	substring = str_html_not_working[0:10]
	my_id_85 = re.findall('[0-9]+', substring)
	listToStr = ' '.join(map(str, my_id_85))
	print(listToStr)  
	
	exit() 


	if my_id_85 != None:
		print("id:_" + my_id_85.group(1))
	else:
		print("no regex found")

	my_id_142 = re.search('<td>(.*)\. ', str_html_working)
	if my_id_142 != None:
		print("id:_" + my_id_142.group(1))
	else:
		print("no regex found")

	'''

	#phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	phone_num_regex = re.compile(r'(\(\d{3}\))(\d{3}-\d{4})')

	mo = phone_num_regex.search("My number is (435)434-5456.")
	#print('phone number found: ' + mo.group(1))

	area_code, number = mo.groups()

	#print (area_code)

	heroRegex = re.compile(r'Batman|Tina Fey')

	mo1 = heroRegex.search('Batman and Tina Fey')

	#print(mo1.group())
	mo2 = heroRegex.search('Tina Fey and Batman')
	#print(mo2.group())

	batRegex = re.compile(r'Bat(man|mobile|girl|bat)')
	mo3 = batRegex.search('The Batmobile broke a Batbat')
	#print(mo3.group())
	#print(mo3.group(1))


	batWomanRegex = re.compile(r'Bat(wo)?man')
	mo1 = batWomanRegex.search('Batman is all right')
	mo2 = batWomanRegex.search('Batwoman is really cool')
	#print(mo1.group())
	#print(mo2.group())

	phoneRegex2 = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
	mo1 = phoneRegex2.search('My number is 434-434-3456')
	#print(mo1.group())
	#mo2 = phoneRegex2.search('My number is 434-4345')
	#print(mo2.group())

	batRegex2 = re.compile(r'Bat(wo)*man')
	mo1 = batRegex2.search('The Batman was here')
	#print(mo1.group())


	le_html = '<td>243. Dusty Springfield’s <i>Dusty in Memphis</i><br/>by Warren Zanes<br/>Buy from Bloomsbury: <a href="http://bloomsbury.com/us/dusty-springfields-dusty-in-memphis-9780826414922/">US</a> | <a href="http://bloomsbury.com/uk/dusty-springfields-dusty-in-memphis-9780826414922/">UK/Europe</a><br/><a href="http://www.amazon.com/Dusty-Springfields-Memphis-Thirty-Three/dp/0826414923/ref=sr_1_1?ie=UTF8&amp;qid=1391619650&amp;sr=8-1&amp;keywords=33+1%2F3+Dusty+in+Memphis">Amazon</a></td>'


	regex_id = re.compile(r'\d+')
	mo = regex_id.search(le_html)
	print(mo.group())