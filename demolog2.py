#!/usr/bin/python
#Purpose of this script: 
#Date: Wed Mar 20 18:48:37 IST 2019
#Author of this script: Srinivav
#Reviewer of this script: 
import logging

logging.basicConfig(level=logging.WARNING)

logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('This message comes from one module')
logger2.warning('And this message comes from another module')
#!/usr/bin/python
#Purpose of this script: 
#Date: Wed Mar 20 18:49:06 IST 2019
#Author of this script: Srinivav
#Reviewer of this script: 
