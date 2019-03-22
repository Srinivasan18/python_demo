#!/usr/bin/python
#Purpose of this script: 
#Date: Fri Mar 22 13:27:15 IST 2019
#Author of this script: SRinivav
#Reviewer of this script: 
import logging
 
logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")
 
try:
    raise RuntimeError
except Exception, err:
    log.exception("Error!")
