#!/usr/bin/env python3
from typing import List,Dict
from sys import stdout,stderr,argv
from io import StringIO
from re import findall

def usage():
    stderr.write("usage: ./foil.py [option] [args]\n")
    stderr.write("Options and arguments:\n")
    stderr.write(" -f     : Factors and sorts the results of the foil\n")
    stderr.write(" -e     : Shows the output in a \"<input> = <output>\" format. Output is still affected by -f\n")
    stderr.write(" --     : Specifies all strings after it to be combined into an input. When not given, only the last string is used\n")
    stderr.write(" [args] : Strings which contain word groups (text surrounded by parens or '/'). Text not in word groups is ignored\n")
    exit(-1)

if len(argv) == 1:
    usage()

user_input: int = 1
factor: int = 0
show_equals: int = 0
output = stdout
for i,arg in enumerate(argv[1:]):
    if arg == "-f":
        factor = 1
        output = StringIO()
    elif arg == "-e":
        show_equals = 1
    elif arg == "-":
        user_input = 1
    elif arg == "--":
        user_input = 0
        inp: str = ' '.join(argv[i+2:])
        break
    else:
        user_input = 0
        inp: str = arg

if user_input:
    stderr.write("Enter words here: ")
    inp: str = input()
words: List[str] = [i[1:-1] for i in findall(r'[\(/].*?[\)/]', inp)]

if not words:
    stderr.write("No words to foil\n")
    exit(-1)
elif len(words) == 1:
    stdout.write((inp + " = " if show_equals else "") + words[0] + "\n")
    exit(0)

if not factor and show_equals:
    stdout.write(inp + " = ")
for i,word in enumerate(words):
    for mult in word:
        for sword in words[i+1:]:
            for char in sword:
                output.write(mult + char)
output.write('\n')

if factor:
    value: str = output.getvalue()
    # Remove newline
    value = value[:-1]
    output.close()
    factors: Dict[str, int] = {}
    for char in value:
        if char in factors:
            factors[char] += 1
        else:
            factors[char] = 1
    variables = sorted(factors, key=factors.__getitem__, reverse=True)
    if show_equals:
        stdout.write(inp + " = ")
    for i,var in enumerate(variables):
        if factors[var] == 1:
            stdout.write(var)
        else:
            stdout.write("(" + var + "^" + str(factors[var]) + ")")
    stdout.write('\n')
