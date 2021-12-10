#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 13:50:57 2021

@author: fennieliang
"""

from week14_class import Data_process as dp
from lesson_02_class import Text_process as tp
 
db = dp.db_conn()

mycursor = db.cursor()
# dynamic select table
table_name=input("Select a table:")

sql = f"DESCRIBE {table_name} "

mycursor.execute(sql)
for x in mycursor:
    string = str(x)
    s1 = string.split(',')
    final_string=tp.doc_clean(s1[0])
    print(final_string)
