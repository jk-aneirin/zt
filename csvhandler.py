#!/usr/bin/python
import redis
import csv
import sys
import socket
import dns.resolver
from multiprocessing import Pool
def Getmailbox(f):
	csvfile=file(f,'rb')
	reader=csv.reader(csvfile)
	for line in reader:
		mailbox.append(line[1])
	csvfile.close()
	mailbox.pop(0)
	for i in mailbox:
		original.add(i)

'''def Getip(realm):
	try:
		socket.gethostbyname(realm)
		return True
	except socket.gaierror:
		return False
'''
def Getmx(realm):
       try:
               dns.resolver.query(realm,'MX')
               return True
       except:
               return False

def Extractservername(mailbox):
	index=mailbox.index('@')
	return mailbox[index+1:]
	
def Filtermailbox(l):
	for i in l:
		for j in patterns:
			if j in i:
				rub.add(i)
			else:
				continue
def Getresult(x):
                s=Extractservername(x)
                if Getmx(s):
                        return x
                else:
			pass

def Getlastrealm(mailbox):
	index=mailbox.index('@')
        return mailbox[index:]

def Insertredis(realm):
## Shell redis-cli -h 192.168.2.182 -p 6379  -a passwd -x zadd filter:not_by_hanqi:mail:suffix:list 0
	r=redis.StrictRedis(host='192.168.2.182',password='password')
	r.zadd('filter:not_by_hanqi:mail:suffix:list',0,realm)
	#r=redis.StrictRedis(host='192.168.70.160',port=6379)
	#r.zadd('list',0,realm)
if __name__=="__main__":
	patterns=['aliyun.com','pp.con','qq.con','126.con','.cm','qq.om','qq.o','qq.cn','qq.com.cn','126.vip.com','163.c0m','189.cn','189.CN','21cn.net','263.net.cn','2b1.com.cn','3achieve.com']
	mailbox=[]
	resultmailbox=[]
	original=set()
	rub=set()
	diff=set()
	L1=[]
	L2=[]
        mailboxrealm=set()
	
	filename=sys.argv[1]
	Getmailbox(filename)
	Filtermailbox(mailbox)
	diff=original-rub
	p=Pool(50)
	L1=p.map(Getresult,list(diff))
	#print L2=[i for i in L1 if i not in [None]]	
	for i in L1:
		if i not in [None]:
			mailboxrealm.add(Getlastrealm(i))
#	print mailboxrealm
	#fl=open('/root/domainList.txt','w')
        #for idmail in mailboxrealm:
        #    fl.write(idmail)
        #    fl.write("\n")
        #fl.close()
        for idmail in mailboxrealm:
		#Insertredis(idmail)
		print idmail
	
