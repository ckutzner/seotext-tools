#!/usr/bin/env python3
""" call with text to be analyzed as argument"""
import sys
import analysis
import results

# read in keywords, build dictionaries
bodykw = {} # keywords in body text, pattern: Keyword, target count
h1kw = {} # keywords in h1
h2kw = {} # keywords in h2
metakw = {} # keywords in meta description
titlekw = {} # keywords in title tag


# count words
text = open(sys.argv[0]).read() 
wordcount = len(text.split())
print("Total wordcount:\t{}".format(wordcount))
