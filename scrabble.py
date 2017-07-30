#!/usr/bin/env python

import sys

def convertChar(char, flag):
    if (char == ' ' and flag):
        return ":space:"
    elif char == ' ':
        return ":scrabble-blank:"
    elif char.isalpha():
        if (flag and (char != 'a' and char != 'b' and char != 'o' and char != 'x' and char != 's' and char != 'm' and char != 'v')):
            return ":" + char + ":"
        else:
            return ":scrabble-" + char + ":"
    elif isvalid(char):
        return ":scrabble-" + getnames(char) + ":" 
    elif char.isnumeric():
        return ":scrabble-" + char + ":"
    else:
        return char

def isvalid(char):
    return (char=='\'' or char=='*' or char== ')' or char== '(' or char== ':' or char== ',' or char== '$' or char== '!' or char== ';' or char== '/' or char== '^' or char == '?' or char == '@' or char == '&' or char == '.')

def getnames(char):
    if char=='\'':
        return "ap"
    elif char=='*':
        return "as"
    elif char==')':
        return "bp"
    elif char==':':
        return "cl"
    elif char==',':
        return "cm"
    elif char=='$':
        return "do"
    elif char=='!':
        return "ep"
    elif char=='(':
        return "fp"
    elif char==';':
        return "sc"
    elif char=='/':
        return "sl"
    elif char=='^':
        return "up"
    elif char=='&':
        return "am"
    elif char=='@':
        return "at"
    elif char=='?':
        return "qm"
    elif char=='.':
        return "pr"



def scrabblify(input, aliasFlag):
    output = ""
    for ch in input:
        output += convertChar(ch, aliasFlag)

    return output
