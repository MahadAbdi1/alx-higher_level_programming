#!/usr/bin/python3
# Replaces all occurrences of an element by another in a new list

def search_replace(my_list, search, replace):
    return list(map(lambda e: e if e != search else replace, my_list))
