#!/bin/bash


for i in `cat ./apache_log.log | awk '{print $1}' | sort -u`;
 do  
 getcount=`cat ./apache_log.log |grep $i | grep GET |wc -l`;
 echo "$i : GET=$getcount "
 done
