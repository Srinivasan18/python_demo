#!/usr/bin/python
#Purpose of this script: 
#Date: Wed Mar 20 20:02:36 IST 2019
#Author of this script: Srinivav
#Reviewer of this script: 
import argparse

parser=argparse.ArgumentParser(
    description='''Welcome to logger script ''',
    epilog="""END.""")
parser.add_argument('-n PUT', type=int, default=200, help='PUT logs')
parser.add_argument('-n POST', type=int, default=500, help='POST logs')
parser.add_argument('-n GET', type=int, default=401, help='GET logs')
args=parser.parse_args()
