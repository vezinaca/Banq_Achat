#!/usr/bin/env python3

import re

phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo_matching_object = phone_num_regex.search("this is my phone 545-454-4444")
print (mo_matching_object.group()) #545-454-4444
print(mo_matching_object.group(1)) #545
print(mo_matching_object.groups()) #('545', '454-4444')
area, number = mo_matching_object.groups()
print(number)

phone_num_parent = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo_tes = phone_num_parent.search('voici le (545) 545-5456')
print(mo_tes.group())

pipe_match = re.compile(r'Batman|Tina')
mo_pipe = pipe_match.search('Tina can do this')
print(mo_pipe.group()) #Tina

pipe_batman = re.compile(r'Bat(man|mobile|copter)')
mo_bat = pipe_batman.search("The Batcopter got sooooo drunk")
print(mo_bat.group()) #Batcopter
print(mo_bat.group(1)) #copter

question_mark = re.compile(r'Bat(wo)?man')
mo_batwoman = question_mark.search("Batman was here")
print("non pe: " + mo_batwoman.group())


mo_batman_question = question_mark.search('Batman was here shit shit')
print("oui shit hit: " + mo_batman_question.group())
print("non pe: " + mo_batwoman.group())

star_re = re.compile(r'Bat(wo)*man')
mo_starBat = star_re.search('Batwowowoman is a gigigigigirl')
print(mo_starBat.group())

plus_re = re.compile(r'Bat(wo)+man')
mo_plus = plus_re.search('Batwowoman is under the bridge')
print(mo_plus.group())

ha_re = re.compile(r'(ha){3,5}?')
mo_ha = ha_re.search('hahahahaha')
print (mo_ha.group())

#=================================================
#findAll returns list
print("################find all")

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
list_findAll = phoneNumRegex.findall("work: 543-545-6654 and cell is 665-333-4444")
for thing in list_findAll:
	print(thing)

