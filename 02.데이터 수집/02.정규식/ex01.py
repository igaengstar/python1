#정규식(Regular Expression, regex) / 문자열에서 규칙을 찾아내는 도구

#match
'''import re

pattern = re.compile('ca.e')
while True:
    word = input('단어> ')
    if word == '': break

    match = pattern.match(word)
    if match:
        print('일치')
    else: 
        print('불일치')'''

#search
import re

pattern = re.compile('se$')
while True:
    word = input('단어> ')
    if word == '': break

    match = pattern.search(word)
    if match:
        print('일치')
    else: 
        print('불일치')