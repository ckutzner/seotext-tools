""" module for printing out results """
import analysis

def pretty(fn,wc_target,*args):
    """function for pretty-printing results, fn is the filename"""
    words = analysis.wordcount(fn,wc_target) # calls analysis, saves results in a tuple - should it be moved to the main program file?
    print("Here is where you are with {}:\n".format(fn)) # preamble
    print(55*"="+"\n") # separator line + newline
    print("Total word count:\t{}\t{}".format(words[0], words[1]))
    print(55*"="+"\n") # separator line + newline
    # maybe move all the decorative stuff & structure to a template file?

if __name__ == "__main__": #test function
    pretty("testdata/testtext.md",500)
