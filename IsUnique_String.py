# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:02:59 2024

@author: Ramandeep
"""

#code to check if string is unique
def is_unique_3(input_str):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i,"")
        else:
            return False
    return True

my_str = "apple s"
print(is_unique_3(my_str))