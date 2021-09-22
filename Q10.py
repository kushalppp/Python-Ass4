#!/usr/bin/python3

fruits={}
a=1
x=int(input("enter a no:"))
while a<=x:
 key = a 
 value = key*key
 fruits[key]= value
 a=a+1
print(fruits)

Output:-
enter a no:5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}