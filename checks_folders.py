# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 10:40:35 2018

@author: Sarth.choudhary
"""
import os
from pathlib import Path
from shutil import copy2
test_dir = r"C:\Users\Sarth.choudhary\Desktop\Test"
dir_list = os.walk(test_dir)
dir_list1 = list(dir_list)
#n_folders = len(dir_list)
#for n in dir_list1:
#    print(n)
file_list = []
list_of_all_files = []
for i in range(len(dir_list1)):
    if not dir_list1[i][2] == []:
        a = Path(dir_list1[i][0])
        b = (dir_list1[i][2])
        list_of_all_files.append(b) #list all files
        b = ''.join(b)
        file_path = a / b
        file_list.append(file_path)
for j in range(len(file_list)):
    copy2(file_list[j], r'C:\Users\Sarth.choudhary\Desktop\destination')