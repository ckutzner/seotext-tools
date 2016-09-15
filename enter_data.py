"""module for entering data into the jobs and keyword database"""

# def readstuff(file, dictindex, *args):
    """quick-and-dirty function to read stuff in, args: file, dictionary index, prepared dictionaries; requires module re"""
    name = ''
    tc = 300 # default value
    with open(file, 'r') as data:
        lines = data.readlines()
    for l in lines:
        if ': ' in l:
            x = l.split(': ')
            dictindex.append(x[0])
        elif re.search('^\d{3,5}$',l):
            tc = int(l)
        else: 
            name = l
    return name, dictindex, tc

if __name__ == "__main__":
    print("This module is not functional yet!")
