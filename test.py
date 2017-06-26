import re

testList = ['cats', 'dogs']
searchStr = ' '.join(testList)

print searchStr


toFind = 'dog'
key = ('r\'/(.' + toFind + '.)\w+/g\'')      #want to find this word/part of word

print key

# print toFind
match = re.match( key, searchStr, re.M|re.I)
print match
