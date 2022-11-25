"""
Homework 6 Python Programming 2022
17th of Nov 2022
Volentir Alexandra, 3A5
"""

import re
import os

from typing import List, Dict, Tuple


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


def __contains_one_attr(xml_line: str, attr: Tuple[str, str]) -> bool:
    return re.search(rf'{attr[0]}\s*=\s*"{attr[1]}"(\s|>)', xml_line) is not None


def exercise4(path: str, attributes):
    """
    Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns
    those elements that have as attributes all the keys in the dictionary and values the corresponding values.
    For example, if attrs={"class": "url", "name": "url-form", "data-id": "item"} the items selected will be those tags
    whose attributes are class="url" si name="url-form" si data-id="item".
    """

    with open(path, "r") as xml_document:
        tags = set()
        xml_doc_lines = xml_document.readlines()
        for line in xml_doc_lines:
            xml_elem_list = re.findall(r'<\w.*?>', line)

            for xml_elem in xml_elem_list:
                tag = None
                found = re.search(r'<(.*?) |<(.*?)>', xml_elem)
                if found:
                    tag = found.group(found.lastindex)

                attr_list = re.findall(r'\s.*?\s*=\s*".*?"|\s.*?\s*=\s*\'.*?\'', xml_elem)
                current_attrs = {}
                for attr in attr_list:
                    attr_split = attr.split('=')
                    name = attr_split[0].strip()
                    value = attr_split[1].strip().strip('\"\'')

                    if name in attributes:
                        current_attrs[name] = value
                if current_attrs == attributes:
                    tags.add(tag)
        return tags


def exercise5(path, attributes):
    """
    Write another variant of the function from the previous exercise that returns those elements that have
    at least one attribute that corresponds to a key-value pair in the dictionary.
    """
    with open(path, "r") as xml_document:
        tags = set()
        xml_doc_lines = xml_document.readlines()
        for line in xml_doc_lines:
            xml_elem_list = re.findall(r'<\w.*?>', line)

            for xml_elem in xml_elem_list:
                tag = None
                found = re.search(r'<(.*?) |<(.*?)>', xml_elem)
                if found:
                    tag = found.group(found.lastindex)

                attr_list = re.findall(r'\s.*?\s*=\s*".*?"|\s.*?\s*=\s*\'.*?\'', xml_elem)

                for attr in attr_list:
                    attr_split = attr.split('=')
                    name = attr_split[0].strip()
                    value = attr_split[1].strip().strip('\"\'')

                    if name in attributes and attributes[name] == value:
                        tags.add(tag)
        return tags


def exercise6(string):
    """
    Write a function that, for a text given as a parameter, censures words that begin and end with vowels.
    censor_funcship means replacing characters from odd positions with *.
    """
    words = string.split()
    new_words = []
    vocals = "aeiouAEIOU"
    for word in words:
        if re.match(f"^[{vocals}]\w*[{vocals}]$", word):
            sliced_word = list(word)
            for index in range(0, len(word)):
                if index % 2 == 1:
                    sliced_word[index] = "*"
            word = "".join(sliced_word)
        new_words.append(word)
    new_text = " ".join(new_words)

    return new_text


def exercise7(cnp: str) -> bool:
    if not (
            re.search(
                r"^[0-8]\d\d((0[1-9])|(1[0-2]))((0[1-9])|([12]\d)|(3[01]))\d{6}$", cnp
            )
    ):
        return False
    magic_sum = sum(
        list(
            int(zipped[0]) * int(zipped[1]) for zipped in zip("279146358279", cnp[:-1])
        )
    )
    return int(cnp[-1]) == (magic_sum % 11 if magic_sum % 11 != 10 else 1)


def exercise8(folder_path: str, regx: str):
    """8.Write a function that recursively scrolls a directory and displays those
    files whose name matches a regular expression
    given as a parameter or contains a string that matches the same expression.
    Files that satisfy both conditions will be prefixed with ">>"""
    dir_list = os.listdir(folder_path)
    try:
        for path in dir_list:
            if os.path.isfile(path):
                found = False
                if re.match("^" + regx + "$", path.split("/")[-1]):
                    found = True
                with open(path, "r+") as file:
                    lines = file.read()
                    if re.findall(regx, lines):
                        if found:
                            print(f">>{path}")
                            continue
                        else:
                            print(f"{path}")
                            continue
                    print(path)
    except Exception as e:
        SystemError(e)
