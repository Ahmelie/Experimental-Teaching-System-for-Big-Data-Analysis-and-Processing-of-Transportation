# -*- coding:utf-8 -*-
# author:
# -*- coding: utf-8 -*-
'''百度坐标转换'''
import urllib
import math
import csv
import json
import pandas as pd



if __name__ == '__main__':
    input_file='scope.csv'
    output_file = open('scope.json', 'w')
    csv_col_name = list(pd.read_csv(input_file,encoding='gb18030').columns)  # 取到列名
    csv_data = csv.DictReader(open(input_file, 'r'), csv_col_name)  # 以字典方式读取csv数据
    next(csv_data)  # 取出第一条数据也就是表头
    
    output_file.write('{"data":[')
    for rows in csv_data:
            cur='{"ID":"'+str(rows['FID'])+'","Point":"'+str(rows['CenLon'])+','+str(rows['CenLon'])+'"},'
            #print(cur)
            output_file.write(cur)

    output_file.write(']}')
    output_file.close()
