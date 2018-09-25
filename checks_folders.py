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
#temp_dir = os.path.join(source_dir, 'temp')
#if not os.path.exists(temp_dir):
#    os.makedirs(temp_dir)
for i in range(len(dir_list1)):
    if not dir_list1[i][2] == []:
        a = Path(dir_list1[i][0])
        dir_list2 = dir_list1[i][2]
        for k in range(len(dir_list2)):
            b=dir_list2[k]
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
#        copy2(file_list[j], temp_dir)        
        [name,ext] = os.path.splitext(file_name)
        cntr = 1
        new_file_name = name + '-{}'.format(cntr)  + ext
        dest_file_name = dest_dir / new_file_name
        while os.path.isfile(dest_file_name):
            cntr = cntr + 1
            new_file_name = name + '-{}'.format(cntr)  + ext
            dest_file_name = dest_dir / new_file_name
        new_file_name_with_dir = os.path.dirname(file_list[j]) + "\\" + new_file_name
        os.rename(file_list[j], new_file_name_with_dir)
        copy2(new_file_name_with_dir, dest_dir)
#os.rmdir(temp_dir)