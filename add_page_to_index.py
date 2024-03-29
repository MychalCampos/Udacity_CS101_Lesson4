# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 22:14:46 2015
# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.
@author: Mychal
"""


index = []


def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword, [url]])


def add_page_to_index(index, url, content):
    words = content.split()
    for i in words:
        add_to_index(index, i, url)

add_page_to_index(index, 'fake.text', "This is a test")
print index
# >>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
# >>> ['test',['fake.text']]]
add_page_to_index(index, 'real.test', "This is not a test")
print index    