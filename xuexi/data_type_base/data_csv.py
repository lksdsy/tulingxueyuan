'''
CSV(Comma-Separated Value) 逗号分隔符
CSV文件是由任意的数据记录组成，记录间以某种换行符分割，每行记录由换行符组合
eg: 1001,xxx,18,China
CSV可以用exal表格打开
'''

import csv

headers = ['ID', 'UserName', 'Age', 'Country']
rows = [
    (1001, 'zs', 18, 'Beijing'),
    (1002, 'ls', 28, 'Chengdu'),
    (1003, 'qs', 38, 'Shanghai')
]


with open('text.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)



