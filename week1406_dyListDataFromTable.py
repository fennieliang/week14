#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:41:03 2021

@author: fennieliang
"""
from week14_class import Data_process as dp
 
db = dp.db_conn()

mycursor = db.cursor()
# dynamic select table
table_name=input("Select a table:")

mycursor.execute(f"SELECT * FROM {table_name}")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)