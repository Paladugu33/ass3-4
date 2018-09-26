import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
db=mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="admin",
                database="mydb"
                )
mycursor=db.cursor()
#sql1= "select violation_description from violations;"
sql="select INS1.activity_date,VIO1.violation_description,INS1.facility_zip from INS1,VIO1 where INS1.serial_number=VIO1.serial_number;"
mycursor.execute(sql)
#res1 = mycursor.fetchall()
res = mycursor.fetchall()
ls=[]
for i in res:
  emplist=[]
 # print("date",i[0])
#  print("description",i[1])
 # print("zip_code",i[2])
#  print("city",i[3])
  emplist.append(i[0])
  emplist.append(i[1])
  ls.append(emplist)

print (ls)
colmns=["Date","Description"]
df=pd.DataFrame(ls,columns=colmns)
df['Date']=pd.to_datetime(df['Date'])
df['month'] = df['Date'].dt.month
df['year'] = df['Date'].dt.year
#print (df['month'].count())
#print (df)
#print (list(df['month']))
months_map = {1: 'Jan', 2: 'Feb' , 3:'march' , 4:'april',5:'may',6:'june',7:'july',8:'august',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
def mapper(month):
    return months_map[month]
print (df['month'].count())
'''
grouped = df.groupby('month')
for i in range(1,13):
    if i in list(df['month']): 
        print ('for month %s violations are: '%mapper(i))
        print (grouped.get_group(i).count()['month'])
    else :
        pass
'''



dic={}
grouped = df.groupby('month')
for i in range (1,13):
    if i in list(df['month']):
        #dic.append(mapper(i))
        dic[mapper(i)] = grouped.get_group(i).count()['month']
    else :
        pass
    
print (dic)



'''
#print(df)
g = df.groupby(pd.DatetimeIndex(df['Date']).month)
print(g)
#df['month'] = pd.DatetimeIndex(df['Date'])
print(df['month'])
'''

x = dic.keys()
y = dic.values()
plt.title("average violations per month")
plt.xlabel("months")
plt.ylabel("number of violations per month")
plt.bar(x,y,label = dic.keys(),color=['red','blue','green','black'])
plt.legend()
plt.show()


