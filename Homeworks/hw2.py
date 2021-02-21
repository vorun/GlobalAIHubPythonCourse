# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 22:00:37 2021

@author: Orhun
"""
stdnames = []
stdgrades =[[],[],[],[],[]]


std1= str(input("please enter a student name:"))
stdnames.append(std1)
std1midterm = int(input("please enter students midterm grade"))
stdgrades[0].append(std1midterm)
std1final =int(input("please enter students final grade"))
stdgrades[0].append(std1final)
std1project = int(input("please enter student project grade"))
stdgrades[0].append(std1project)

std2= str(input("please enter a student name:"))
stdnames.append(std2)
std2midterm = int(input("please enter students midterm grade"))
stdgrades[1].append(std2midterm)
std2final =int(input("please enter students final grade"))
stdgrades[1].append(std2final)
std2project = int(input("please enter student project grade"))
stdgrades[1].append(std2project)

std3= str(input("please enter a student name:"))
stdnames.append(std3)
std3midterm = int(input("please enter students midterm grade"))
stdgrades[2].append(std3midterm)
std3final =int(input("please enter students final grade"))
stdgrades[2].append(std3final)
std3project = int(input("please enter student project grade"))
stdgrades[2].append(std3project)

std4= str(input("please enter a student name:"))
stdnames.append(std4)
std4midterm = int(input("please enter students midterm grade"))
stdgrades[3].append(std3midterm)
std3final =int(input("please enter students final grade"))
stdgrades[3].append(std3final)
std3project = int(input("please enter student project grade"))
stdgrades[3].append(std3project)

std5= str(input("please enter a student name:"))
stdnames.append(std5)
std5midterm = int(input("please enter students midterm grade"))
stdgrades[4].append(std5midterm)
std5final =int(input("please enter students final grade"))
stdgrades[4].append(std5final)
std5project = int(input("please enter student project grade"))
stdgrades[4].append(std5project)



info = {}
info[std1] = stdgrades[0]
info[std2] = stdgrades[1]
info[std3] = stdgrades[2]
info[std4] = stdgrades[3]
info[std5] = stdgrades[4]

av =[]
a = info[std1]
std1av = sum(a) / 3
av.append(std1av)

b = info[std2]
std2av = sum(b) / 3
av.append(std2av)
     
     
c = info[std3]
std3av = sum(c) / 3
av.append(std3av)
          
         
d = info[std4]
std4av = sum(d) / 3
av.append(std4av)
              
e = info[std5]
std5av = sum(e) / 3
av.append(std5av)
                   
                   
if max(av)== std1av:
                      print("conguratulations",std1,"!")
elif max(av)== std2av:
                      print("conguratulations",std2,"!")
elif max(av)== std3av:
                      print("conguratulations",std3,"!")
elif max(av)== std4av:
                      print("conguratulations",std4,"!")
elif max(av)== std5av:
                      print("conguratulations",std5,"!")






















