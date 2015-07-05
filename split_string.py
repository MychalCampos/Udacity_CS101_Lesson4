# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 15:23:38 2015
# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.
@author: Mychal
"""


# # First attempt. This works, but this is UGLY!
# def split_string(source, splitlist):
#    # first construct a list of the positions of the delimiters in splitlist
#    pos = []
#    i = 0
#    while i < len(source):
#        if source[i] in splitlist:
#            pos.append(i)
#        i = i + 1
#    # account for text that comes after the final delimiter in source
#    if pos[len(pos)-1] < len(source) - 1:
#        pos.append(len(source))
#    # construct list of strings split by delimiters in splitlist
#    strsplit = []
#    j = 0
#    k = 0
#    while k < len(pos):
#        # ignore extra blank spaces which will have length 0
#        if len(source[j:pos[k]]) >= 1:
#            strsplit.append(source[j:pos[k]])
#        j = pos[k] + 1
#        k = k + 1
#    return strsplit


# Instructor's solution. This is better and more intuitive!
def split_string(source, splitlist):
    output = []
    atsplit = True  # at a split point
    for char in source:  # iterate through string by each character
        if char in splitlist:
            atsplit = True
        else: 
            if atsplit:  # if we're at a split point
                output.append(char)
                atsplit = False  # char appended is not at a split point
            else: #  if we're in the middle of a word
                # add character to the word that is not yet complete 
                # [-1] corresponds to the last entry in output
                output[-1] = output[-1] + char
    return output                
                

out = split_string("This is a test-of the,string separation-code!", " ,!-")
print out
# >>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
# >>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name, Last Name, Street Address, City, State, Zip Code", ",")
print out
# >>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
