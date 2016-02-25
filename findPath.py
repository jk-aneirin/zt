#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib2
import sys
import re

'''Get Content of Url'''
def getHtml(url):
	try:
		page=urllib2.urlopen(url)
		html=page.read()
		return html
	except AttributeError:
		print 'The Revision ID is not found'

'''Get Modification Record Url'''
def retrieveUrl(html,sn):
	soup=BeautifulSoup(html)
	ol_tags=soup.find_all('ol')
	for ol_tag in ol_tags:
		for li_tag in ol_tag.find_all('li'):
			value=li_tag.get('value')
			if sn==value:
				return topurl+li_tag.find_all('a')[1].get('href')
	else:
		print "The Revision ID is not found"
		exit(0)
		
def getResult():
	keys=[]
	content=[]
	url=topurl+'changes'
	resurl=retrieveUrl(getHtml(url),revid)
	print "The URL you needed:\n"+resurl+"\n"
	ht=getHtml(resurl)
	soup=BeautifulSoup(ht)
	for j in soup.table.nextSibling.next.next.nextSibling.find_all('a'):
		if not j.has_attr('href') and not j.has_attr('name'):
			m=unicode(j.string)
			content.append(m)
			n=re.match(r"\d{5}",m)
			if n:	
				keys.append(m)
	s=' '.join(content)
	v=re.split('\d{5}',s)[1:]
	suc=dict(zip(keys,v))
	for k in suc.keys():
		if unicode(revid)==k:
			return suc[k]	
def trans():
	with open("./mid.txt","r") as f:
        	for line in f:
                	i=str(line)
               		if i.endswith("js\n") or i.endswith("jsp\n") or i.endswith("html\n"):
                        	print i[36:],
                	elif i.endswith("java\n") and i.startswith("/branches/zhipin-V1/src/main/java/"):
                        	print "WEB-INF/classes/"+i[34:-5]+"class"	
def main():
	path=[]
	s=getResult().strip()
	path=s.split(' ')
	print "Original paths:\n"
	for i in path:
             print i
	print "\n"
	print "***Modified paths:\n"
	with open("./mid.txt","w") as f:
		for i in path:
			f.write(i)
			f.write("\n")
	trans()
if __name__=="__main__":
	#project=sys.argv[1]
	project="eyas_zhipin_test"
	
	revid=sys.argv[1]
	topurl="http://192.168.2.236:9876/job/"+project+'/'
	main()
	
