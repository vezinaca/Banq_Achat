#!/usr/bin/env python3

import re



if __name__ == '__main__':

	str_html_working = "<td>142. The Wild Tchoupitoulas’ <em>The Wild Tchoupitoulas</em><br/>by Bryan Wagner"
	str_html_not_working = "<td>85. Portishead’s <i>Dummy</i><br/>by RJ Wheaton<br/>Buy from Bloomsbury: <a href="
	
	my_id_85 = re.search('<td>(.*)\. ', str_html_not_working)
	if my_id_85 != None:
		print("id:_" + my_id_85.group(1))
	else:
		print("no regex found")

	my_id_142 = re.search('<td>(.*)\. ', str_html_working)
	if my_id_142 != None:
		print("id:_" + my_id_142.group(1))
	else:
		print("no regex found")