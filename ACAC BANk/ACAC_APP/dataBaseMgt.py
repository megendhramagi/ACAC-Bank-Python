import mysql.connector
from django.shortcuts import render,redirect
import random

def openDb():
     mycon=mysql.connector.connect(
     host='localhost',
     username='root',
     password='1234',
     database='acac'
     )
     return mycon
     
def registerDB(rData):
     mycon=openDb()
     mycursor=mycon.cursor()
     try:
          sqlQ="insert into acac values(%s,%s,%s,%s,%s,%s)"
          v=(rData.get('gAccNo'),rData.get('gPinNO'),rData.get('name'),rData.get('age'),rData.get('phone'),rData.get('deposit'))

          mycursor.execute(sqlQ,v)
          mycon.commit()
          return True
     except Exception:
          return False
     finally:
          mycon.close()

def loginDB(lCredentials):
     mycon=openDb()
     mycursor=mycon.cursor()
     try:
          sqlQ="select *from acac where accNo="+lCredentials['accountNo']+" and pinNo="+lCredentials['pin']+";"
          mycursor.execute(sqlQ)
          result=mycursor.fetchall()
          rCount=mycursor.rowcount
          if(rCount!=0):
               return True,result
          else:
               return False,""
     except Exception:
          return False
     finally:
          mycon.close()

def randomm(lenn):
     if lenn==6:
          result=random.randint(100000,999999)
          return result
     elif lenn==4:
          result=random.randint(1000,9999)
     return result

def updateAmt(accNo,amt):
     mycon=openDb()
     mycursor=mycon.cursor()
     sqlQ="update acac set availAmt= "+str(amt)+" where accNo= "+str(accNo)+";"
     try:
          mycursor.execute(sqlQ)
          mycon.commit()
          return True
     except Exception as e:
          print(e)
          return False
     finally:
          mycon.close()

def updateTransferAmt(taccNo,tamt):
     mycon=openDb()
     mycursor=mycon.cursor()
     sqlQ="update acac set availAmt= availAmt +"+str(tamt)+" where accNo= "+str(taccNo)+";"
     try:
          mycursor.execute(sqlQ)
          mycon.commit()
          return True
     except Exception as e:
          print(e)
          return False
     finally:
          mycon.close()     

     





