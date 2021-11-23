# -*- coding:utf-8 -*-
# author:
# -*- coding: utf-8 -*-
'''百度坐标转换'''
import urllib
import math
import csv
import json
import pandas as pd
from copy import deepcopy
from urllib.request import urlopen,quote
from collections import Counter

def find_all_index(arr, item):
    return [i for i, a in enumerate(arr) if a == item][0]
def make_dict(hatmapData_file,codeList_file):
    csv_col_name = list(pd.read_csv(input_file,encoding='gb18030').columns)  # 取到列名
    csv_data = csv.DictReader(open(input_file, 'r'), csv_col_name)  # 以字典方式读取csv数据
    next(csv_data)  # 取出第一条数据也就是表头
    list1 = []
    list2=[]
    lenth=10
    num=0
    for rows in csv_data:
        cur=str('%.6f' % float(rows['MAP_LON']))+','+str('%.6f' % float(rows['MAP_LAT']))
        print(cur)
        if cur in list1:
            print('yes')
            print(find_all_index(list1,cur))
            list2[find_all_index(list1,cur)]=list2[find_all_index(list1,cur)]+1
        else:
            list1.append(cur)
            list2.append(0)
        #word_counts1 = Counter(temp)
        #word_counts=word_counts1+word_counts
        #word_counts.update(str('%.6f' % float(rows['MAP_LON']))+', '+'%.6f' % float(rows['MAP_LAT']) )
        num=num+1
        #cur={num:{ 'center': { 'lng': '%.6f' % float(rows['MAP_LON']), 'lat':  '%.6f' % float(rows['MAP_LAT']) }}}

        if num>10:
            return list1,list2

if __name__ == '__main__':
    input_file='taxi.csv'
    hatmapData_file = open('hatmapData.json', 'w')
    codeList_file = open('codeList.json', 'w')
    csv_col_name = list(pd.read_csv(input_file,encoding='gb18030').columns)  # 取到列名
    csv_data = csv.DictReader(open(input_file, 'r'), csv_col_name)  # 以字典方式读取csv数据
    next(csv_data)  # 取出第一条数据也就是表头
    list1 = []
    list2=[]
    lenth=10
    num=0
    jump=10
    patch=0
    for rows in csv_data:
        #print(jump)
        if jump==100:
            cur=str('%.6f' % float(rows['MAP_LON']))+','+str('%.6f' % float(rows['MAP_LAT']))
            #print(cur)
            if cur in list1:
                #print('yes')
                #print(find_all_index(list1,cur))
                list2[find_all_index(list1,cur)]=list2[find_all_index(list1,cur)]+1
            else:
                list1.append(cur)
                list2.append(0)
        elif jump==0:
            jump=101
        jump=jump-1
        num=num+1
        if num>999 and num%1000==0:
            patch=patch+1
            print(patch)
    
    hatmapData_file.write('{"data":[')
    codeList_file.write('{')
    for i in range(len(list1)):
        temp=list1[i].split(',')
        codeList_file.write('"'+str(i)+'":{ "center": { "lng": "'+str(temp[0])+'", "lat":"'+str(temp[1])+'" }},')
        for j in range(list2[i]+1):
            hatmapData_file.write
            hatmapData_file.write('{ "name": "'+str(i)+'"},')
    
    hatmapData_file.write(']}')
    codeList_file.write('}')
    codeList_file.close()
    hatmapData_file.close()
    #json.dump(make_dict(input_file), output_file, ensure_ascii=False)
   # output_file.close()
