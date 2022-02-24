# arr = [3, 3, 1, 2, 1, 4, 1, 3, 4, 7, 8]

# def thing(arr):
#     dic = {}

#     for i in range(len(arr)):
#         if arr[i] in dic:
#             dic[arr[i]] += 1
#         else: dic[arr[i]] = 1
    
#     it = []
#     #items = sorted(dic.items(), key = lambda item: item[1], reverse = False)
#     keys = sorted(dic.items(), key = lambda item: (item[1], item[0]), reverse = True)

#     return keys

# print(thing(arr))

import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

Ha HaHa

MetaCharacters (Need to be escaped!):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'Start')

matches = pattern.match(sentence)

print(matches)

# for match in matches: 
#     print(match)
