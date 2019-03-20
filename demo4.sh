#!/bin/bash

 for i in `cat ./apache_log.log | awk '{print $1}' | sort -u`;
 do
 getcount=`cat ./apache_log.log |grep $i | grep GET |wc -l`;
 putcount=`cat ./apache_log.log |grep $i | grep PUT |wc -l`;
 postcount=`cat ./apache_log.log |grep $i | grep POST |wc -l`;
 delcount=`cat ./apache_log.log |grep $i | grep DELETE |wc -l`;
 echo "$i : GET=$getcount , PUT=$putcount , POST=$postcount , DELETE=$delcount "
 done
