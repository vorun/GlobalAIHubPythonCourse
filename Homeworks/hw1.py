# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:13:03 2021

@author: Orhun
"""
a = []
b = []
c = []


for num in range(3):
 
 import random as rnd

 notprime = True
 while notprime:

  x = rnd.randint (1,100)

  if x > 1:
 
    
     for i in range(2, x):
 
        
         if (x % i) == 0:
            
            
             break
     else:
        notprime = False
        a.append(x)

print(a)

for num in range(3):
 
 notprime = True
 while notprime:

  x = rnd.randint (1,100)

  if x > 1:
 
    
     for i in range(2, x):
 
        
         if (x % i) == 0:
            
            
             break
     else:
        notprime = False
        b.append(x)
print(b) 

for num in range(3):
 
 notprime = True
 while notprime:

  x = rnd.randint (1,100)

  if x > 1:
 
    
     for i in range(2, x):
 
        
         if (x % i) == 0:
            
            
             break
     else:
        notprime = False
        c.append(x)
 
print(c)    
