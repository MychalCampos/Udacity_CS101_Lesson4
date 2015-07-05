# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 21:32:05 2015
# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.
@author: Mychal
"""


index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]


def lookup(index, keyword):
    for i in index:
        if i[0] == keyword:
            return i[1]
    return []

print lookup(index, 'udacity')
# >>> ['http://udacity.com','http://npr.org']    