#!/usr/bin/env python3

import codecs
import sys
import re


if len(sys.argv) < 2:
    sys.exit(1)

infile = codecs.open(sys.argv[1], encoding='utf-8')

header = infile.readline()
header = header.strip()
header_fields = header.split(",")
num_fields = len(header_fields)

print(header)

eol_re = re.compile(',"[^"]*"\s*"')
cur_str = ""
for line in infile:
    line = line.strip()
    cur_str += line
    if (eol_re.search(cur_str)):
        print(cur_str[:-1])
        cur_str = '"'

