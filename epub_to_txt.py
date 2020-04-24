###### MODIFY CODE HERE ########
path = "path/to/epubs/directory/"
output = "name_of_output_file.txt"
###### END OF MODIFY CODE HERE ###########

from epub_conversion.utils import open_book, convert_epub_to_lines
import os
import re
from string import digits
cleanr = re.compile('<.*?>')
remove_digits = str.maketrans('', '', digits)
final = []
for filename in os.listdir(path):
    ret = []
    book = open_book(path + filename)
    lines = convert_epub_to_lines(book)
    count = 0
    length = len(lines)
    maxim = length - 300
    for i in range(len(lines)):
        
        cleantext = re.sub(cleanr, '', lines[i])
        sos = cleantext[:-1].rstrip()
        sos = sos.translate(remove_digits)
        if sos.rstrip() != "" and count > 100 and count < maxim:
            ret.append(cleantext[:-1].lstrip())
        count += 1
    for i in range(len(ret)):
        line = ret[i]
        sos = re.split(r'\W+', line)
        if len(sos) > 2:
            final.append(line)
f= open(output,"w+")
exceptcount = 0
for i in range(len(final)):
    try:
        f.write(final[i])
    except:
        exceptcount += 1
f.close()
