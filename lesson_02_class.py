#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:34:15 2021

@author: fennieliang
"""


import re

class Text_process: 
  
    def doc_length(string):
        return len(string)
 
    def doc_split_word(string):
        words = re.split('[\W_]',string) #import re package first
        return words  
    
    def doc_clean(string):
        c_string =re.sub(r'[\W]',' ', string)#replace non-word character from the string
        c_string =re.sub(r' +',' ', c_string).strip()
        return c_string

    def bag_word(words):  
        counts = dict()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        
        return counts

    def find_name(string):
        matches = re.finditer('([A-Z][a-z]+\s){1,}', string)
        return matches

    def find_digit(string):
        matches = re.finditer('(\d+,){0,}(\d+.)(\d+)', string)
        return matches

#view class and method in a tree structure
#click View>Panes>Outlines
#on top right-coner of the panes, tick show all files