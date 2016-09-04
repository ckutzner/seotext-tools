#!/usr/bin/env python3
""" call with text to be analyzed and target wordcount as argument for now; later, target word count shall be read from data file!"""
import sys
import os
import os.path
import analysis
import results
import enter_data
import dbsetup
import sqlite3

# read variable targetcount from args - for now; in finished software that should be read from data db!
infile = sys.argv[1]
targetcount = int(sys.argv[2])

# read in keywords, build dictionary for job in question from database 
bodykw = {} # keywords in body text, pattern: Keyword, target count
h1kw = {} # keywords in h1
h2kw = {} # keywords in h2
metakw = {} # keywords in meta description
titlekw = {} # keywords in title tag

# set database file
if not "data" in os.listdir(): # check if directory data exists, if not, create
    os.mkdir("data") 
dbfile = 'data/db.sqlite'

# check if dbfile exists, if not, call dbsetup
if os.path.isfile(dbfile) == False:
    setup_db.db_setup(dbfile)

# create text object to be passed to functions; returns text as list! 
with open(infile, "r") as f:
    text = f.read().split()

# Call ALL THE functions :) and maybe classes!
wc = analysis.wordcount(text, targetcount)
#analysis.kwcount( )
results.pretty(infile, wc)

# test 
if __name__ == "__main__":
#    results.pretty(infile, wc)
    print("This module is not functional yet!")
