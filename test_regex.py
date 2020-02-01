#!/usr/bin/env python3

import re



if __name__ == '__main__':

	str_html = "<td>85. Portishead’s <i>Dummy</i><br/>by RJ Wheaton<br/>Buy from Bloomsbury: <a href="
	my_id = re.search('<td>(.*)\. ', str_html)
	if my_id != None:
		print("id:_" + my_id.group(1))
	else:
		print("no regex found")