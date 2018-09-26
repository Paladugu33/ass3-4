
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import numpy as np
db=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="admin",
                database="mydb"
                )
mycursor=db.cursor()

sql="select INS1.activity_date,VIO1.violation_code,INS1.facility_zip from INS1,VIO1 where INS1.serial_number=VIO1.serial_number;"
mycursor.execute(sql)

res = mycursor.fetchall()
ls=[]
for i in res:
  emplist=[]
 
  emplist.append(i[0])
  emplist.append(i[1])
  emplist.append(i[2])
  ls.append(emplist)


colmns=["Date","code","zip"]
df=pd.DataFrame(ls,columns=colmns)

df['Date']=pd.to_datetime(df['Date'])
df['month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year

months_map = {1: 'Jan', 2: 'Feb' , 3:'march' , 4:'april',5:'may',6:'june',7:'july',8:'august',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
def mapper(month):
    return months_map[month]

dic={}

try:
    for i in range(1,13):
        if i in list(df['month']):
            fd = (df.loc[df['month']==i])
            grouped = fd.groupby('zip')
            zips = set(fd['zip'])
            lst=[]
            for j in zips:
                lst.append(grouped.get_group(j).count()['zip'])
                dic[mapper(i)]=(max(lst)-min(lst))
        
except Exception as e:
    print(e)
print (dic)

x = dic.keys()
y = dic.values()
plt.title("variance of post code per month")
plt.xlabel("months")
plt.ylabel("varience")
plt.bar(x,y,label = dic.keys(),color=['red','blue','green','black'])
plt.legend()
plt.show()


