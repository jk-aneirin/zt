#!/bin/bash
#scripts for dirbakup and upload to ftp server.
#author by xl
#create by 
bakdir=rubpy  #this dir will be backup
date=`date +%F`

cd /root
tar zcf ${bakdir}_${date}.tar.gz ${bakdir}

sleep 1

ftp -n <<- EOF
open 192.168.2.26
user username passwd
bin    #binary mode upload
put rubpy_*.tar.gz
bye
EOF  

rm -rf  rubpy_*.tar.gz
