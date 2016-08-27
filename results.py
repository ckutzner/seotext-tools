""" module for printing out results """

def pretty(fn, wc):
    """function for pretty-printing results, fn is the filename"""
    print("Here is where you are with {}:\n".format(fn)) # preamble
    print(55*"="+"\n") # separator line + newline
    print("Total word count:\t{}\t{}".format(wc[0], wc[1]))
    print(55*"="+"\n") # separator line + newline
    # maybe move all the decorative stuff & structure to a template file?

#if __name__ == "__main__": #test function
#    pretty("testdata/testtext.md",500)
