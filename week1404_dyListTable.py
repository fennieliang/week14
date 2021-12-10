#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:59:07 2021

@author: fennieliang
"""
from week14_class import Data_process as dp
 
db = dp.db_conn()

mycursor = db.cursor()

# dynamic select database and show tables
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)