# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:02:59 2024

@author: Ramandeep
"""

#code to check if string is unique
#defined string alpha having all alphabets and space
#iterating through ecah charcater in string and removing the char if it is alpha
#if char is not in alpha, it means the char is repeated, therefore exit loop and return false else return true at end of for loop
def is_unique(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i,"")
        else:
            return False
    return True

my_str = "apple s"
print(is_unique(my_str))
