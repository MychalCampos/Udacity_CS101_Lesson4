# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 20:02:34 2015
# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]
@author: Mychal
"""


# helper procedure for taking the union between 2 sets
def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


index = []


def add_to_index(index, keyword, url):
    for i in index:
        if i[0] == keyword:
            union(i[1], [url])  # use union in case url already exists
            return
    index.append([keyword, [url]])

add_to_index(index,'udacity', 'http://udacity.com')
add_to_index(index,'computing', 'http://acm.org')
add_to_index(index,'udacity', 'http://npr.org')
print index    