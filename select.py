#!/usr/bin/python

import sys
import time



today = time.strftime("%d/%b/%Y", time.localtime())



def dictify_logline(line):
    split_line = line.split()
    return  {'request_url': split_line[6],'status':split_line[8]}
def generate_log_report(logfile): 
    report_dict = {} 
    for line in logfile:
        line_dict = dictify_logline(line)
        if not "200" in line or not today in line:
            continue
        print line_dict 
    return report_dict 
 
if __name__ == "__main__": 
    if not len(sys.argv) > 1: 
        print __doc__ 
        sys.exit(1) 
    infile_name = sys.argv[1] 
    try: 
        infile = open(infile_name,'r') 
    except ValueError: 
        print "pls specify a  file" 
        sys.exit(1) 
    log_report = generate_log_report(infile) 
    print log_report 
    infile.close() 
