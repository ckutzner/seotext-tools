""" module for text analysis """

def kwcount(infile, keyword, target):
    """count the occurrences of keywords in a text and display total count + evaluation message""" # this is a clear use case for classes!	
    text = open(infile).read() # would perhaps be better to have a text object already passed to the module
    kwc = text.split().count(keyword)
    # keyword count evaluation
    if kwc < target:
        message = "Not there yet!"
    elif kwc > target:
        message = "Over target count"
    else:
        message = "Target count achieved!"
    
    print("Keyword count:\t{} of {}\n\t{}".format(kwc, target, message)) # this printout will be moved to results.py to give a pretty-printed results table once I have figured out how to do that.
    return kwc, message

def wordcount(infile, targetcount):
    """This function counts the words in the text and determines if target word count has been reached or exceeded by more than 35 words.""" #still to be added: function to exclude meta and title section from the word count
    text = open(infile).read() # would perhaps be better to have a text object already passed to the module
    wordcount = int(len(text.split()))
    # different evaluation from keyword count is needed here because keyword count does not have tolerance, wordcount must have or else it's hard to achieve.
    if wordcount < targetcount:
        message = "Not there yet!"
    elif wordcount > targetcount+35:
        message = "Over target count"
    else:
        message = "Target count achieved!"

    print("Total wordcount:\t{}\n\t{}".format(wordcount, message)) # this printout will be moved to results.py to give a pretty-printed results table once I have figured out how to do that.
    return wordcount, message

# test
# if name=="__main__":

