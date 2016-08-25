""" module for printing out results """
import analysis

def pretty(fn,wc_target,*args):
    """function for pretty-printing results, fn is the filename"""
    print("Here is where you are with {}:\n".format(fn)) # preamble
    print(55*"="+"\n") # separator line + newline
    print("Total word count:\t{}\t{}".format(analysis.wordcount(fn,wc_target)[0],analysis.wordcount(fn,wc_target)[1]))
    print(50*"="+"\n") # separator line + newline


if __name__ == "__main__": #test function
    pretty("testdata/testtext.md",500)
