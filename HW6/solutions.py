"""
Homework 6 Python Programming 2022
17th of Nov 2022
Volentir Alexandra, 3A5
"""

import re
import os

days_per_m = [     # days per month
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|1\d|2[0-8])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])"
    ]


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
    with open(path, "r") as f:
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
    with open(path, "r") as f:
        data = f.read()
        lookup = r"(<(\w+) [^>]*(" + r"|".join(
            ["{key}=\"{value}\"".format(key=k, value=v) for k, v in attr.items()]
        ) + r")[^>]*>[^(<\2>)]*</\2>)"
        for match in re.findall(lookup, data):
            res += match[0]
    return res


def censor_func(text):
    text = text.group(0)
    return "".join([text[j] if j % 2 == 0 else "*" for j in range(len(text))])


def exercise6(string):
    """
    Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
    censor_funcship means replacing characters from odd positions with *.
    """
    return re.sub(r"(a|e|i|o|u)\w+(a|e|i|o|u)", censor_func, string)


def get_days(y, m):
    try:
        if int(y) % 4 == 0:
            days_per_m[1] = r"(0[1-9]|1\d|2[0-9])"
        return days_per_m[int(m) - 1]
    except Exception as e:
        raise SystemError(e)


def get_control_digit(d):
    sum = 0
    for i, j in zip("279146358279", d):
        sum += int(i) * int(j)
    sum %= 11
    if sum == 10:
        sum = 1
    return str(sum)


def exercise7(input_text):
    """
    7.Verify using a regular expression whether a string is a valid CNP.
    """
    matches_list = list()
    matches_list.append(r"[1-8]") # first digit
    matches_list.append(r"\d{2}") # year
    matches_list.append(r"(0[1-9]|1[0-2])") # month
    matches_list.append(get_days(input_text[1:3], input_text[3:5])) #day
    matches_list.append(r"(0[1-9]|[1-3]\d|4[0-6]|5[1-2])") # country
    matches_list.append(r"(00[1-9]|0[1-9]\d|\d\d\d)") # random digits
    matches_list.append(get_control_digit(input_text[:-1])) # control digit

    reg_str = r"^"
    for elm in matches_list:
        reg_str += elm
    reg_str += r"$"
    print(reg_str)
    return bool(re.match(reg_str, input_text))


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
                cond1 = re.match(reg, f_path)
                cond2 = re.match(reg, open(f_path, "r").read())
                if cond1 and cond2:
                    list_of_matches.append(">>" + f_path)
                elif cond1 or cond2:
                    list_of_matches.append(f_path)
    except Exception as e:
        SystemError(e)
    return list_of_matches
