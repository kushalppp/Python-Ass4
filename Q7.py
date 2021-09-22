#!/usr/bin/python3

x=[1,4,2,3,5,6,6]
q=len(x)
for a in list(range(q-1)):
 z=x.count(x[a])
 if z==2:
  del x[a]
print(x)

Output:-
[1, 4, 2, 3, 5, 6]