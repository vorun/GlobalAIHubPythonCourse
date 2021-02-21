# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 01:56:41 2021

@author: Orhun
"""

def prime_first(x):

 
  
    if x > 1:
 
    
     for i in range(2, x):
 
        
         if (x % i) == 0:
            
            
             break
     else:
        
           print(x)
     
def prime_second(x):

  if x > 1:
 
    
     for i in range(2, x):
 
        
         if (x % i) == 0:
            
            
             break
     else:
        
           print(x)
     
     
for x in range(0,1000):
    if x < 500:
        prime_first(x)
    else: 
        prime_second(x)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     