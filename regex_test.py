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
mo_batwoman = question_mark.search("Batwoman was here")
print(mo_batwoman.group())

star_re = re.compile(r'Bat(wo)*man')
mo_starBat = star_re.search('Batwowowoman is a gigigigigirl')
print(mo_starBat.group())