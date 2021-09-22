#!/usr/bin/python3

y=[1,2,3]
x=[4,2,6]
q=len(y)
w=len(x)
for a in list(range(q-1)):
 for b in list(range(w-1)):
  if y[a]==x[b]:
   print(y[a],x[b],"common in two list") 

print(x,y)

Output:-
2 2 common in two list
[4, 2, 6] [1, 2, 3]