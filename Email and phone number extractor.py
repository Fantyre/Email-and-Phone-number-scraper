#! python3

import re, pyperclip

Phoneregex = re.compile('''
#345-555-2376  OR (345)-555-2376 OR 555-2376
((
((\d\d\d)|(\(\d\d\d)))?    #Area Code(optional)
(\s|-)                     #Seperator
\d\d\d                     #3 digits
-                     #Seperator
\d\d\d\d)                   #4 digits


''', re.VERBOSE)

Emailregex = re.compile('''
#exa_+.%-mple123@gmail.com
[a-zA-Z0-9._+]+    #name_part
@   #@ sign
[a-zA-Z0-9._+]+    #domain name
\.               # dot
[a-z]{2,}       # upper domain


''', re.VERBOSE)

text = pyperclip.paste()

extractedPhone = Phoneregex.findall(text)
extractedEmail = Emailregex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

result = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(result)