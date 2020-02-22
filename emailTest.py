#!/usr/bin/env python3

import smtplib
from datetime import datetime

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtpObj))
print(smtpObj.ehlo())
smtpObj.starttls()
print(smtpObj.login('racontemoidoncca@gmail.com', 'ZaqWsxcd'))

email_string = 'Subject: New book availibility verification for ' + str(datetime.now()) + '\n'
email_string = email_string + "\nBonjour, \n Voici vos livres"

smtpObj.sendmail('racontemoidoncca@gmail.com', 'vezinaca@gmail.com',
email_string)
smtpObj.quit()