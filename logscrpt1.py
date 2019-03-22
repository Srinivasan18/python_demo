#!/usr/bin/python
#Purpose of this script: 
#Date: Thu Mar 21 14:58:32 IST 2019
#Author of this script: Srinivav
#Reviewer of this script: 
import argparse

parser = argparse.ArgumentParser(description='Process access code.')
parser.add_argument('integers', metavar='-n', type=int, nargs='+',
                    help='include error code along with this option')
parser.add_argument('codes', metavar='error codes', type=int, nargs='+',
                    help='Enter error code 200, 500, 401 with this option')

args = parser.parse_args()
print(args.accumulate(args.integers))
