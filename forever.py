#!/usr/bin/python

import sys
import time

def main_loop():
    while 1:
        print add()
        time.sleep(5)
		
def add():
	return 3 + 6
	
if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)