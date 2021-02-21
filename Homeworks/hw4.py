# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:46:54 2021

@author: Orhun
"""
import random as rnd
words =["english","board","python","keyboard","trade"]
print("possible words:", *words, sep = " ,")
w = rnd.choice(words)
print(w)
x = [] 
for i in range(len(w)):
     x.append("_", )
print(*x, sep = " ")
def split(word):
    
    
    return [char for char in w]
def split(w):
    return [char for char in w]

class word():
    def __init__(self,length,letters):
        self.length = length
        self.letters = letters
            
choosenword = word(len(w),w)

z = 7
j = 6
c = 0
cun = True
while True:

    choosenletter = input(str("please guess a letter"))
    if (choosenletter in split(w)):
       i = split(w).index(choosenletter)
       x[i] = choosenletter
       print(*x, sep = " ")
       
       
       
       
       if (split(w) == (x)) :
           print("you won !")
           cun = False
           break
       else:    
       
           b=j-c
           print("tries left",b)
       
    else :
        c= c+1
        print("wrong guess")
        b=j-c
        print("tries left",b)
        if (b==0):
            print("you lost")
            cun = False
            break


         

    
    
    