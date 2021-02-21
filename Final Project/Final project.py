# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:23:32 2021

@author: Orhun
"""
print("Hello! Welcome to oruns cook book-program! We have 3 recipes for you!")
class recipe:
  def __init__(self, ing1, am1, ing2, am2, ing3, am3, time, heat):
    self.ing1 = ing1
    self.am1 = am1
    self.ing2 = ing2
    self.am2 = am2
    self.ing3 = ing3
    self.am3 = am3
    self.time = time
    self.heat = heat

  def cook(self):
    print("mix", self.am1,"of",self.ing1,"and",self.am2,"of",self.ing2,"and",
          self.am3,"of",self.ing3,"and cook them for",self.time,"with",self .heat)


class soup(recipe):
  def __init__(self,ing1,am1,ing2, am2, ing3, am3, time, heat, spice1, spice2, secret):
   super().__init__(ing1,am1,ing2, am2, ing3, am3, time, heat) 
   self.spice1 = spice1
   self.spice2 = spice2
   self.secret = secret
  def adding(self):
       print("after 10 minutes of cooking add",self.spice1, "and", self.spice2,
             "and last add the secret item",self.secret,"!","oh boy eat this and you're goin places!")




class fries(recipe):
  def __init__(self,ing1,am1,ing2, am2, ing3, am3, time, heat, cheese, ketchup, milkshake):
   super().__init__(ing1,am1,ing2, am2, ing3, am3, time, heat)   
   self.cheese = cheese
   self.ketchup = ketchup
   self.milkshake = milkshake
  def adding(self):
      print("after frying your fries put 2 cups of",self.cheese,
            "on it after that put just a touch of",self.ketchup,
            "now you can dip your fries in",self.milkshake,"and enjoy!you just lost 10 years of your life!")




class meat(recipe):
  def __init__(self,ing1,am1,ing2, am2, ing3, am3, time, heat, döner, lavaş):
   super().__init__(ing1,am1,ing2, am2, ing3, am3, time, heat) 
   self.döner = döner
   self.lavaş = lavaş
    
  def adding(self):
      print("after cooking take your meat and wrap it around with",self.döner,
            "now you wrap that around with",self.lavaş,"just like a tornado! meat is back on the menu!")
      





magicshroomsoup = soup ('mushrooms','4grams','unions','3pieces','water','2leters',
                        '20 minutes','low heat','cumin','pepper','secret')
print("                                          ","MAGİCSHROMSOUP")
magicshroomsoup.cook()
magicshroomsoup.adding()

heartattackfries = fries ('potato',2,'oil','half a leter','spice','2 tea spoons'
                          ,'15 minutes','high heat','nacho cheese','ketchup',
                          'strawberry milkshake')
print("                                        ","HEARTATTACK FRİES")
heartattackfries.cook()
heartattackfries.adding()

meattornado = meat ('chopped chicken','200grams','chopped meat','200 grams',
                    'chopped kokoreç','200 grams','15 minutes',
                    'moderate heat in just a touch of oil','döner','lavaş')
print("                                          ","MEAT TORNADO")
meattornado.cook()
meattornado.adding()

