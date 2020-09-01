# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 17:23:33 2020

@author: Shanu
"""

from random import randint
num=str(randint(100, 999))

print("Welcome to the 3 digit number guessing game \nType \"quit\" to forfeit the game ")




def guess():
    usr=str(input("Input your guess\n"))
     
    if(len(usr)<3):
        print("Enter only three digit number")
        guess()
        
    if(usr=="quit"):
        print("The Number was : "+num+" \nYou lost")
        
        
    if(usr==num):
        print("Superb !!! Number guessed correctly")
        
        
    
    if(usr!=num and usr!='quit'):
        flag=0
        for i in usr:
            
            if i in num:
                a=usr.index(i)
                b=num.index(i)
                if a==b:
                    flag=1
                else:
                    flag=2
                    
        if(flag==1):
            print("Match")
            
        elif(flag==2):
            print("Close")
        else:
            print("No Match")
            
        guess()    
        
guess()         
            
