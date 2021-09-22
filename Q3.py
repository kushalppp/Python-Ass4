#!/usr/bin/python3


x=input("enter a words with space seprator:-")
y=(' '.join(dict.fromkeys(x.split())))
li=list(y.split(" "))
li.sort()
print(li)

Output:-
enter a words with space seprator:-hello world how are you hello world
['are', 'hello', 'how', 'world', 'you']