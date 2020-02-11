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
	substring = str_html_not_working[0:10]
	my_id_85 = re.findall('[0-9]+', substring)
	listToStr = ' '.join(map(str, my_id_85))
	print(listToStr)  

	#print(*my_id_85)
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