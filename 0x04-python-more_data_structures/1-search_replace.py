#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def repl(s):
        return (s if s != search else replace)
    return list(map(repl, my_list))
