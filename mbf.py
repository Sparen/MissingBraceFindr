#!/usr/bin/env python3

# Missing Brace Finder by Andrew Fan
# Hastily thrown together on Dec 9, 2018
# Not guaranteed to work; use at your own risk
# MIT License

# Usage:
# mbf.py <filename>

import sys

def peek(stack):
    if (len(stack) == 0):
        return None
    return stack[len(stack) - 1]

# Parses a file and marks unmatched [({})]
# This function works by reading line by line, character by character, and then appending various characters to a stack if necessary.
# [({})] within comments and strings are ignored.
# When finding an inconsistency, this program assumes that a character was MISSING, pops a control marker off of the stack, and proceeds.
def parsefile(file):
    currline = 0;
    stack = []
    for line in file:
        currline += 1
        currchar = 0
        # If last line was a comment, pop the comment marker
        if peek(stack) == "#":
            stack.pop()
        # Iterate over each line
        for char in line:
            currchar += 1
            if (char == '"' or char == "'") and peek(stack) == char:
                # If encounter a string and we have a matching string marker, pop it off the stack
                stack.pop()
            elif (char == '"' or char == "'") and peek(stack) != "'" and peek(stack) != '"' and peek(stack) != '#':
                # If we encounter a string and we do not have a matching string/comment marker, append it to the stack
                stack.append(char)
            elif peek(stack) == "'" or peek(stack) == '"':
                # If we encounter a non-string and we have a string marker, pass
                pass
            elif char == "#":
                # Ignore comments
                stack.append(char)
            elif peek(stack) == "#":
                pass
            elif char == '[' or char == '(' or char == '{':
                # If we encounter an opening character, append it to the stack
                stack.append(char)
            elif (char == ']' and peek(stack) == '[') or (char == ')' and peek(stack) == '(') or (char == '}' and peek(stack) == '{'):
                # If we encounter a closing character and we have an opening character marker, pop it off the stack
                stack.pop()
            elif (char == ']' and peek(stack) != '['):
                print ("Mismatched bracket at Line " + str(currline) + ", Column " + str(currchar))
                print ("Expected ] but got " + str(char))
                stack.pop()
            elif (char == ')' and peek(stack) != '('):
                print ("Mismatched parentheis at Line " + str(currline) + ", Column " + str(currchar))
                print ("Expected ) but got " + str(char))
                stack.pop()
            elif (char == '}' and peek(stack) != '{'):
                print ("Mismatched brace at Line " + str(currline) + ", Column " + str(currchar))
                print ("Expected } but got " + str(char))
                stack.pop()
            #print (str(currline) + str(stack))
    print ("All Clear")

for i in range(1, len(sys.argv)):
    f = open(sys.argv[i], 'r')
    print ("Now parsing file " + str(sys.argv[i]))
    parsefile(f)
    f.close()
