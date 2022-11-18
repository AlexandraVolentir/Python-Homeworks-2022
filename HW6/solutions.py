"""
Homework 6 Python Programming 2022
17th of Nov 2022
Volentir Alexandra, 3A5
"""

import re
import os


def exercise1(string):
    """
    Write a function that extracts the words from a given text as a parameter.
    A word is defined as a sequence of alpha-numeric characters.
    """
    return re.findall(r"[a-zA-Z\d]+", string)


def exercise2(reg_string, text_string, x):
    """
    Write a function that receives as a parameter a regex string,
    a text string and a whole number x, and returns those long-length
    x substrings that match the regular expression.
    """
    matching = list()
    for elm in re.findall(reg_string, text_string):
        if len(elm) == x:
            matching.append(elm)
    return matching


def exercise3(string, regexes):
    """
    Write a function that receives as a parameter a string of text characters and a list
    of regular expressions and returns a list of strings that match on at least one regular
    expression given as a parameter.
    """
    list_of_matches = list()
    for x in regexes:
        found = re.findall(x, string)
        for y in found:
            if y not in list_of_matches:
                list_of_matches.append(y)
    return list_of_matches


def exercise4(path, attr):
    """
    Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns
    those elements that have as attributes all the keys in the dictionary and values the corresponding values.
    For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags
    whose attributes are class="url" si name="url-form" si data-id="item".
    """
    res_list = list()
    f = open(path, "r")
    parsed_data = f.read()
    lookup = r"(<(\w+)" + r"".join(
        [" {key}=\"{value}\"".format(key=k, value=v) for k, v in attr.items()]
        ) + r">[^</\2>]*</\2>)"
    for match in re.findall(lookup, parsed_data):
        res_list += match[0]
    return res_list


def exercise5(path, attr):
    """
    Write another variant of the function from the previous exercise that returns those elements that have
    at least one attribute that corresponds to a key-value pair in the dictionary.
    """
    res = list()
    f = open(path, "r")
    data = f.read()
    lookup = r"(<(\w+) [^>]*(" + r"|".join(
        ["{key}=\"{value}\"".format(key=k, value=v) for k, v in attr.items()]
    ) + r")[^>]*>[^(<\2>)]*</\2>)"
    for match in re.findall(lookup, data):
        res += match[0]
    return res
