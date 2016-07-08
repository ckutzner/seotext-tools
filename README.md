# SEOText tool aka Copywriter's friend: Have I reached the keyword count yet?
This is a tool for counting occurrences of given words in a given text, occurrences itemized per h1, h2 and paragraph text. If the keyword count is sufficient, the report will display something like "OK".
Dito for the total word count. Target word count can either be one number (then the upper threshold will be word count plus a small percentage) or a range (eg. "280 to 320 words"), an "OK" - or similar message - displayed as well when target is reached.

Input data: structured text file? Database? I didn't decide yet. Probably will use a structured text file first.
So far, this tool processes Markdown (I use it as my default format and then export stuff via pandoc).

Written in Python3.
