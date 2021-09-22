#!/usr/bin/python3

dict1={'1':'1','2':'4'}
dict2={'3':'9','4':'16'}
print(dict1)
print(dict2)
dict1.update(dict2)
print("Two dict are merged:-",dict1)

Output:-
{'1': '1', '2': '4'}
{'3': '9', '4': '16'}
Two dict are merged:- {'1': '1', '2': '4', '3': '9', '4': '16'}