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

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo_vowels = vowelRegex.search("RoboCop east baby food. BABY FOOD")

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

#regexNumbersComa = re.compile(r'\d+|\d,(\d{3})*?') #' 
regexNumbersComa =re.compile(r'^\d{1,3}(,\d{3})*$')
mo_numbers_coma = regexNumbersComa.search('1,234,453')
print(mo_numbers_coma.group())

regex_japan = re.compile(r'^[A-Z]([a-zA-Z])+ Nakamoto$')
mo_japan = regex_japan.search('Satoshi nakamoto')
#print(mo_japan.group())

regex_carol = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)')
mo_carol = regex_carol.search('Alice eats apples')
print(mo_carol.group())

#https://www.w3resource.com/python-exercises/re/python-re-exercise-12.php





#question 12
regex_moreB = re.compile(r'\w+z\w+')
mo_moreB = regex_moreB.search('Hell my nazme is.')
print("#####################33")
print(mo_moreB.group())

#question 13
'''
13. Write a Python program that matches a word containing 'z',
 not at the start or end of the word.
 '''

regex_moreB = re.compile(r'\Bz\B')
mo_moreB = regex_moreB.search('TYhis is azebra.')
print("#####################")
print(mo_moreB.group())

'''
14. Write a Python program to match a string that contains
 only upper and lowercase letters, numbers, and underscores.
'''
#regex_moreB = re.compile(r'\w[a-zA-Z0-9_]\w')
regex_moreB = re.compile(r'^[a-zA-Z0-9_]*$')
mo_moreB = regex_moreB.search('The quick brown fox jumps over the lazy dog.')
print("#####################")
#print(mo_moreB.group())

#17. Write a Python program to check 
#for a number at the end of a string. 
regex_moreB = re.compile(r'.*[0-9]$')
mo_moreB = regex_moreB.search('The quick brown9')
print("#####################")
print(mo_moreB.group())

'''
18. Write a Python program to search the 
numbers (0-9) of length between 1 to 3 in a given string.
'''
regex_moreB = re.compile(r'[0-9]{1,3}')
mo_moreB = regex_moreB.search('The quick brown 2334')
print("#####################")
print(mo_moreB.group())

'''
23. Write a Python program to 
replace whitespaces with an underscore and vice versa
'''
regex_moreB = re.compile(r'_')
mo_moreB = regex_moreB.sub(' ', 'regex_moreB_go home_dance334')
print("#####################")
print(mo_moreB)

'''
25. Write a Python program to convert a 
date of yyyy-mm-dd format to dd-mm-yyyy format.
'''
def change_date_format(dt):
	        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\1-\\2', dt)
dt1 = "2026-07-02"
print("Original date in YYYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


#1. Write a Python program to check that a string contains 
# only a certain set of characters (in this case a-z, A-Z and 0-9)
regex_moreB = re.compile(r'[a-zA-z0-9].*')
mo_moreB = regex_moreB.search('Hell my nazme is.')
print("#####################33")
print(mo_moreB.group())

#2. Write a Python program that matches a 
#string that has an a followed by zero or more b's.

regex_moreB = re.compile(r'ab*?')
mo_moreB = regex_moreB.search('Hell my nab is.')
print("#####################33")
print(mo_moreB.group())

#3.Write a Python program that matches a string that has an a followed by one or more b's
regex_moreB = re.compile(r'ab+')
mo_moreB = regex_moreB.search('Hell my nab is.')
print("#####################33")
print(mo_moreB.group())

#5. Write a Python program that matches a string that has an a followed by three 'b'.
regex_moreB = re.compile(r'ab{3}')
mo_moreB = regex_moreB.search('Hell my nabbb is.')
print("#####################33")
print(mo_moreB.group())

# 6. Write a Python program that matches a string that has an a 
#followed by two to three 'b'
regex_moreB = re.compile(r'ab{2,3}')
mo_moreB = regex_moreB.search('Hell my nabb is.')
print("#####################33")
print(mo_moreB.group())

# 7. Write a Python program to 
#find sequences of lowercase letters joined with a underscore.

regex_moreB = re.compile(r'^[a-z]+_[a-z]+$')
mo_moreB = regex_moreB.search('asdf_fffe')
# aab_cbbbc
print("#####################33")
print(mo_moreB.group())

#8 .Write a Python program to find 
#the sequences of one upper case letter followed by lower case letters.
regex_moreB = re.compile(r'[A-Z][a-z]+')
mo_moreB = regex_moreB.search('asadf aBjlkj fdfd')
print("#####################33")
print(mo_moreB.group())

# 9. Write a Python program that 
#matches a string that has an 'a' followed by anything, ending in 'b'. 

regex_moreB = re.compile(r'a(.*)b$')
mo_moreB = regex_moreB.search('accddbbjjjb')
print("#####################33")
print(mo_moreB.group())

#https://regexone.com/lesson/line_beginning_end
