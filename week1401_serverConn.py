#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 12:54:47 2021

@author: fennieliang
"""

from week14_class import Data_process as dp
host = dp.host_conn()
mycursor = host.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)