#!/bin/sh
PATH=/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/java/latest/bin:/usr/local/php/sbin/:/usr/local/php/bin/:/home/xuliang/bin
SRCFILE=$1
DECFILE=$2
USERNAME="xuliang"
IPPREFIX="192.168.2."
HOSTS=(61 62 63 33 34 43 44 130 134 151)
#HOSTS=(61 62 63)
for i in ${HOSTS[@]};do
        scp /home/xuliang/$SRCFILE $USERNAME@$IPPREFIX$i:~/
done
