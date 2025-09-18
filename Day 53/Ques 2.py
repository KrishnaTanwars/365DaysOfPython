# Question: Given a valid XML document, print the maximum level of nesting. The root is at level 0.

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)
