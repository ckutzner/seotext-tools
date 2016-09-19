"""module for entering data into the jobs and keyword database"""

import re

def readstuff(dfile, dictindex, *args):
    """quick-and-dirty function to read stuff in, args: file, dictionary index, prepared dictionaries; requires module re"""
    name = ''
    tc = 300 # default value
    with open(dfile, 'r') as data:
        lines = data.readlines()
    for l in lines:
        if re.match('\d{3,5}', l):
            tc = int(l)
        elif ': ' in l:
            dictindex.append(l.split(': ')[0])
        else: 
            name = l
    return name, dictindex, tc

if __name__ == "__main__":
    print("This module is not functional yet!")
