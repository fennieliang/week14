#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:21:57 2021

@author: fennieliang
"""
from week14_class import Data_process as dp
 
db = dp.db_conn()

mycursor = db.cursor()

# dynamic select database and create a table

table_name=input("Name a table:")
mycursor.execute(f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

