# Ideas & Issues for seotext tools

## strictly modular programming
* move reading in of keywords \& building of dictionaries to separate module 

## keyword count
* further check that needs to be done: check if one keyword in the list is a substring of any other, and if so, add the kw count of the longer kw to the one of the shorter. no idea how that can be done!
* split text into headlines and body - probably requires regex \& reading text via readlines (except for meta and title section - multiline mode!) - this module should probably be moved to analysis - idea: Leave out the part about meta and title for now. not many customers will ask me for that.
* idea: build syntax funnel \& appropriate regexes for different formats (md, bbcode)
* possible extension: count for bold keywords

## reuse functions
* build evaluation function for message in alalysis module
* move tolerance in word count evaluation into function call for eval function
