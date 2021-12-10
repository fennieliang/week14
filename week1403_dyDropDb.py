#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:51:21 2021

@author: fennieliang
"""
from week14_class import Data_process as dp
host = dp.host_conn()
mycursor = host.cursor()

# dynamic drop database

database=input("Enter database:")
mycursor.execute(f"DROP DATABASE IF EXISTS {database}")

mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)