#!/bin/bash
PATH=/usr/lib/courier-imap/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/java/latest/bin:/home/xuliang/bin
PG=/usr/bin/pgrep
PID=$($PG master)
if [ -z $PID ];then
    echo 1  #postfix down
else
    echo 0   #postfix ok
fi
