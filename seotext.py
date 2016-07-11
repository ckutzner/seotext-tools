#!/usr/bin/env python3
""" call with text to be analyzed and target wordcount as argument"""
import sys
import analysis
import results

# read variable targetcount from args
infile = sys.argv[1]
targetcount = int(sys.argv[2])

# read in keywords, build dictionaries
bodykw = {} # keywords in body text, pattern: Keyword, target count
h1kw = {} # keywords in h1
h2kw = {} # keywords in h2
metakw = {} # keywords in meta description
titlekw = {} # keywords in title tag

# Call ALL THE functions :)
analysis.wordcount(infile, targetcount)
