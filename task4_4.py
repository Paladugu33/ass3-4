# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:23:02 2018

@author: hmohan
"""

import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

db = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password = 'admin',
                        database = 'mydb'
                        )
mycursor = db.cursor()

# for MCDONALDS
sql="""SELECT INS1.program_name as name,VIO1.violation_code as v_code,INS1.activity_date as date,COUNT(activity_date) FROM INS1 INNER JOIN VIO1 ON INS1.serial_number=VIO1.serial_number WHERE INS1.program_name like "%MCDONALDS%" GROUP BY month(INS1.activity_date)"""
mycursor.execute(sql)
myresult = mycursor.fetchall() 
lis=[] 
for i in myresult:
    emplis=[]
    emplis.append(i[0])
    emplis.append(i[1])
    emplis.append(i[2])
    emplis.append(i[3])
    lis.append(emplis)
#print (lis)
columns = ['name','code','date','count']
df1=pd.DataFrame(lis,columns=columns)

df1['date']=pd.to_datetime(df1['date'])
mon=df1['date'].dt.month
months_map = {1: 'Jan', 2: 'Feb' , 3:'march' , 4:'april',5:'may',6:'june',7:'july',8:'august',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
def mapper(month):
    return months_map[month]
lst=[]
for i in mon:
    lst.append(mapper(i))

df1['month']=lst

x=df1['month']
y=df1['count']
plt.title(' MCDONALDS')

plt.subplot(2,1,1)
plt.bar(x,y)

# for burger king

bql="""SELECT INS1.program_name as name,VIO1.violation_code as v_code,INS1.activity_date as date,COUNT(activity_date) FROM INS1 INNER JOIN VIO1 ON INS1.serial_number=VIO1.serial_number WHERE INS1.program_name like "%BURGER KING%" GROUP BY month(INS1.activity_date)"""
mycursor.execute(bql)
myresult = mycursor.fetchall() 
lis=[] 
for i in myresult:
    emplis=[]
    emplis.append(i[0])
    emplis.append(i[1])
    emplis.append(i[2])
    emplis.append(i[3])
    lis.append(emplis)
#print (lis)
columns = ['name','code','date','count']
df1=pd.DataFrame(lis,columns=columns)

df1['date']=pd.to_datetime(df1['date'])
mon=df1['date'].dt.month
months_map = {1: 'Jan', 2: 'Feb' , 3:'march' , 4:'april',5:'may',6:'june',7:'july',8:'august',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
def mapper(month):
    return months_map[month]
lst=[]
for i in mon:
    lst.append(mapper(i))

df1['month']=lst

x=df1['month']
y=df1['count']
plt.title('BURGER KING')

plt.subplot(2,1,2)
plt.bar(x,y)
plt.show()
