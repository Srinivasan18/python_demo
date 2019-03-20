#!/bin/bash

helo=`cat ./apache_log.log | awk '{print $1}' | sort  -u`
#echo  "${helo[@]:1}"
echo -n "helo[0] = "
echo ${helo}
while true
 do
 cat ./apache_log.log | grep "$i" | grep GET| wc -l
 echo $i "======================================"
 cat ./apache_log.log | grep "$i" | grep PUT |wc -l
 echo $i "=========================================="
 
done 
