#!/usr/bin/env python

import random
import MySQLdb
import datetime
from time import gmtime, strftime

from sbhs_server.credentials as credentials

db = MySQLdb.connect(host="credentials.DB_HOST",   	        ## your host, usually localhost ##
                     user="credentials.DB_USER",         		## your username ##
                     passwd="credentials.DB_PASS", 		## your password ##
                     db="credentials.DB_NAME")     		## name of the data base ##

## print "Opened database successfully"

## Execution of querry
cursor5=db.cursor()
cu1=db.cursor()
querry1='SELECT * FROM tables_booking'
cu1.execute(querry1)

## Datetime used when script runs
nowDate=datetime.datetime.now().date()
nowTime=str(datetime.datetime.now().time())
SplittedTime=nowTime.split(":")
NowdaTe=str(nowDate)
NowdaTe=NowdaTe.strip()   ## To remove extra spaces strip is used##


CurrentAccountIdList=[]
BookedSlotId=[]

for DateTimeInBooking in cu1:
	nn=str(DateTimeInBooking[6])
	daTe = nn[0:11]
	tiMe=nn[11:13]
	daTe=daTe.strip()
	
	if daTe==NowdaTe and int(SplittedTime[0])+1==int(DateTimeInBooking[3]):
		CurrentAccountIdList.append(int(DateTimeInBooking[2]))
		BookedSlotId.append(int(DateTimeInBooking[3]))
#print BookedSlotId,CurrentAccountIdList


querry2='SELECT *FROM tables_account'
cu2=db.cursor()
cu2.execute(querry2)


RequiredMidList=[]
for AccountIdFromTablesAccnt in cu2:
	var=AccountIdFromTablesAccnt[0]
	
	for Id in range(len(CurrentAccountIdList)):
		if long(CurrentAccountIdList[Id])==(AccountIdFromTablesAccnt[0]):
			RequiredMidList.append(int(AccountIdFromTablesAccnt[9]))

#print RequiredMidList

SuperUserMidList=[Mid for Mid in range(1,41)]
#print SuperUserMidList

MidsTobeBooked=[mId for mId in SuperUserMidList if mId not in RequiredMidList]
#print MidsTobeBooked

for BookMid in range(len(MidsTobeBooked)):
	ToInsert=[int((MidsTobeBooked[BookMid]))+40,int(SplittedTime[0])+1,(datetime.datetime.now()),(datetime.datetime.now()),(nowDate)]
	cursor5.execute("INSERT INTO tables_booking(account_id,slot_id,created_at,updated_at,booking_date) VALUES(%s,%s,%s,%s,%s)",ToInsert)
	db.commit() ## To update the table Changes in database ##		

## Closing all the object of Cursor
cu1.close() 
cu2.close()
cursor5.close()
db.close()
## print "database closed successfully"
