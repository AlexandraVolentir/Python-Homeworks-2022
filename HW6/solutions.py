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
    lookup = r"(<(\w+)" + r"".join([" {key}=\"{value}\"".format(key=k, value=v) for k, v in attr.items()]
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
    lookup = r"(<(\w+) [^>]*(" + r"|".join(["{key}=\"{value}\"".format(key=k, value=v) for k, v in attr.items()]
        ) + r")[^>]*>[^(<\2>)]*</\2>)"
    for match in re.findall(lookup, data):
        res += match[0]
    return res


def censor(content):
    content = content.group(0)
    text_len = len(content)
    res = ""
    for j in range(text_len):
        if j % 2 == 0:
            res += content[j]
        else:
            res += "#"
    return res


def exercise6(string):
    """
    Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
    censor_funcship means replacing characters from odd positions with *.
    """
    return re.sub(r"(a|e|i|o|u)\w+(a|e|i|o|u)", censor, string)


def exercise8(path, reg):
    """8.Write a function that recursively scrolls a directory and displays those
    files whose name matches a regular expression
    given as a parameter or contains a string that matches the same expression.
    Files that satisfy both conditions will be prefixed with ">>"""
    list_of_matches = list()
    try:
        for r, d, f in os.walk(path):
            for x in f:
                f_path = os.path.join(r, x)
                if re.match(reg, f_path) and re.match(reg, open(f_path, "r").read()):
                    to_append = ">>" + f_path
                    list_of_matches.append(to_append)
                elif re.match(reg, f_path) or re.match(reg, open(f_path, "r").read()):
                    to_append = ">>" + f_path
                    list_of_matches.append(to_append)
    except Exception as ex:
        SystemError(ex)
    return list_of_matches
