#!/usr/bin/python
#Purpose of this script: 
#Date: Fri Mar 22 13:28:07 IST 2019
#Author of this script: Srinivav
#Reviewer of this script: 
import logging
 
#----------------------------------------------------------------------
def main():
    """
    The main entry point of the application
    """
    logging.basicConfig(filename="mySnake.log", level=logging.INFO)
    logging.info("Program started")
    result = otherMod.add(7, 8)
    logging.info("Done!")
 
if __name__ == "__main__":
    main()
