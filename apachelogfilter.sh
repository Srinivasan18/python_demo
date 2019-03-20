#!/bin/bash   
#Purpose of this script: Filter apache logs 
#Date: Wed Mar 20 14:24:40 IST 2019
#Author of this script: Srinivav
#Reviewer of this script: 

#address=`cat ./apache_log.log | awk '{print $1}' | sort  -u`
#echo $address | sort

file="./apache_log.log"
while read line
do
    $line | awk '{print $1}' | sort  -u
done

