#!/usr/bin/python3

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
d4={}
for i in d1.keys():
 for j in d2.keys():
  if i==j:
   x=d1.get(i)
   y=d2.get(i)
   d3[i]=x+y
  if i!=j:
   x=d1.get(i)
   y=d2.get(j)
   d4[i]=x 
   d4[j]=y
d4.update(d3)
print(d4)

Output:-
{'a': 400, 'b': 400, 'd': 400, 'c': 300}
 