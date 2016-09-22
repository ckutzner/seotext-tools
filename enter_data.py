"""module for entering data into the jobs and keyword database"""

import re

def readstuff(dfile, h1, h2, body):
    """quick-and-dirty function to read stuff in, args: file, prepared dictionaries for h1, h2 and body; requires module re"""
    name = ''
    tc = 300 # default value
    with open(dfile, 'r') as data:
        lines = data.readlines()
    for l in lines:
        if re.match('\d{3,5}', l):
            tc = int(l)
        else:
            # dict filling function goes here
            if l.split(': ')[0] == 'h1': 
                # fill that dictionary -> make auxiliary function!
            if l.split(': ')[0] == 'h2':
                # fill that dictionary -> make auxiliary function!
            if =l.split(': ')[0] = 'body':
                # fill that dictionary -> make auxiliary function!
    return tc

if __name__ == "__main__":
    print("This module is not functional yet!")
