#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:57:51 2021

@author: fennieliang
inprogress
"""


from week14_class import Data_process as dp
import json

host = dp.host_conn()
mycursor = host.cursor()

# dynamic create database
database=input("Enter database:")
mycursor.execute(f"CREATE DATABASE {database}")

mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

    
 
