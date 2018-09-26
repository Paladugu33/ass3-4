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
sql="""SELECT INS1.facility_state,VIO1.violation_code as v_code,INS1.activity_date as date,COUNT(activity_date) FROM INS1 INNER JOIN VIO1 ON INS1.serial_number=VIO1.serial_number WHERE INS1.facility_state like "%CA%" GROUP BY month(INS1.activity_date)"""
mycursor.execute(sql)
myresult = mycursor.fetchall()
lst=[]
for i in myresult:
    emplst=[]
    emplst.append(i[0])
    emplst.append(i[1])
    emplst.append(i[2])
    emplst.append(i[3])
    lst.append(emplst)
col=['state','code','date','count']
df=pd.DataFrame(lst,columns=col)
df['date']=pd.to_datetime(df['date'])
mon=df['date'].dt.month
months_map = {1: 'Jan', 2: 'Feb' , 3:'march' , 4:'april',5:'may',6:'june',7:'july',8:'august',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
def mapper(month):
    return months_map[month]
lst=[]
for i in mon:
    lst.append(mapper(i))
df['month']=lst

x=df['month']
y=df['count']
xlabel=('months')
ylabel=('count per month')
plt.bar(x,y,color=['red','brown'])
plt.show()




