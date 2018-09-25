# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 10:40:35 2018

@author: Sarth.choudhary
"""
import os
from pathlib import Path
from shutil import copy2
from ntpath import basename
#from os.path import isfile
source_dir = r"C:\Users\Sarth.choudhary\Desktop\Test"
dest_dir = r'C:\Users\Sarth.choudhary\Desktop\destination'
dir_list = os.walk(source_dir)
dir_list1 = list(dir_list)
file_list = []
temp_folder = os.path.join(source_dir, 'temp')
for i in range(len(dir_list1)):
    if not dir_list1[i][2] == []:
        a = Path(dir_list1[i][0])
        b = (dir_list1[i][2])
        b = ''.join(b)
        file_path = a / b
        file_list.append(file_path)

for j in range(len(file_list)):
    file_name = basename(file_list[j])
    dest_dir = Path(dest_dir)
    file_path = dest_dir / file_name
    if not os.path.isfile(file_path):           #1 no overwrites
        copy2(file_list[j], dest_dir)   #move vs copy
    else:
        [name,ext] = os.path.splitext(file_name)
        new_file_name = name + '-1' + ext
        new_file_name_with_dir = os.path.dirname(file_list[j]) + "\\" + new_file_name
        copy2()
        os.rename(file_list[j], new_file_name_with_dir)
        copy2(new_file_name_with_dir, dest_dir)