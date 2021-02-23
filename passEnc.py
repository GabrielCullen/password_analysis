#!/usr/bin/env python

'''
Requires 3 arguments to be passed
- arg 1 input file of text (each password on a new line)
- arg 2 output file for advanced output
- arg 3 output file for simple output
'''

'''

CREATED BY GABRIEL CULLEN
https://github.com/GabrielCullen/


'''

#this could be made significantly cleaner, feel free to optimize if you like :D

import sys
import decimal

# Output filenames -
fileA = sys.argv[2]
fileB = sys.argv[3]


# Encoding of format : [a-z]{2}[0-9]{2}[A-Z]{2}[s]{2}
def encodeA(file):
    f = open(file, 'r', encoding='utf-8')
    lines = f.readlines()

    # Handle output file
    g = open(fileA, "w")
    g.write("")
    g.close()
    output_file = open(fileA, "a")

    # Iterate through each line
    for line in lines:
        output_line = str("")
        charset = str("")
        last_char = str("")
        count = 0
        for char in line:
            if last_char == "":
                count = 1
                charset = handleCharA(char)
            elif char == last_char:
                count += 1
            elif char == "\n":
                output_line += str(charset) + "{" + str(count) + "}"
            else:
                output_line += str(charset) + "{" + str(count) + "}"

                charset = handleCharA(char)
                count = 1
            last_char = char
        output_file.write(output_line + "\n")
    else:
        output_line += str(charset) + "{" + str(count) + "}"
        output_file.write(output_line)
    f.close()
    output_file.close()
    cleanupFile(fileA)
    countUnique(fileA)


def handleCharA(char):
    if char == "u":
        return str("U")
    elif char == "l":
        return str("L")
    elif char == "d":
        return str("D")
    elif char == "s":
        return str("S")


# Encoding of format : L+D+U+S+
def encodeB(file):
    f = open(file, 'r')
    lines = f.readlines()

    # Handle output file
    g = open(fileB, "w")
    g.write("")
    g.close()
    output_file = open(fileB, "a")

    for line in lines:
        output_line = ""
        charset = ""
        last_char = ""
        for char in line:
            if last_char == "":
                charset = handleCharB(char)
            elif char == "\n":
                output_line += str(charset)
            elif char != last_char:
                output_line += str(charset)
                charset = handleCharB(char)
            last_char = char
        output_file.write(output_line + "\n")
    else:
        output_line += str(charset)
        output_file.write(output_line)
    output_file.close()

    cleanupFile(fileB)
    countUnique(fileB)


def handleCharB(char):
    if char == "u":
        return "U+"
    elif char == "l":
        return "L+"
    elif char == "d":
        return "D+"
    elif char == "s":
        return "S+"


def countUnique(file):
    f = open(file, "r")
    lines = f.readlines()
    f.close()

    unique = {}
    line_count = 0
    ordered_list = []
    max_entry_len = 0
    print("Counting uniques")
    for line in lines:
        line_count += 1
        if len(line.strip()) > max_entry_len:
            max_entry_len = len(line.strip())
        if line.strip() not in unique:
            unique[line.strip()] = 1
        else:
            unique[line.strip()] += 1

    s = '{0:<%d}\t->\t{1}' % max_entry_len
    
    while len(unique) > 0:
        max_count = 0
        max_entry = ""
        for entry in unique:
            if unique[entry] > max_count:
                max_count = unique[entry]
                max_entry = entry
        unique.pop(max_entry)
        ordered_list.append(s.format(max_entry, str(max_count) +
                                     " / " + str(line_count) + " = " + str(decimal.Decimal(max_count) / decimal.Decimal(line_count) * 100) + " %\n"))
    f = open(file, "w")
    print("Sorting")
    f.writelines(ordered_list)


def cleanupFile(file):
    g = open(file, "r")
    lines = g.readlines()
    g.close()

    last_line = lines[-1]
    w = open(file, "w")
    w.writelines([item for item in lines[:-2]])
    w.write(last_line)
    w.close()


def main():
    # Handle input file
    file = sys.argv[1]
    encodeA(file)
    encodeB(file)


if __name__ == "__main__":
    main()
