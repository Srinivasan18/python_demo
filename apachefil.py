#!/usr/bin/python
#Purpose of this script: Filter apache logs
#Date: Wed Mar 20 15:13:22 IST 2019
#Author of this script: Srinivav
#Reviewer of this script: 
import os
f = open('apache_log.log', "r")
#lines = f.readlines()
lines = list(f)
#print(lines)
while lines:
	print(lines)
f.close()
