"""
Homework 1 Python Programming 2022
Date: 11 Oct 2022
© Volentir Alexandra, 3A5

The requirements can be found at: https://sites.google.com/site/fiipythonprogramming/laboratories/lab-1?authuser=0
"""
import re


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def exercise1():
    """Finds the gcd of multiple numbers read from the console"""

    list_of_numbers = []
    n = int(input("Enter number of elements : "))
    if n < 2:
        n = 2
    for i in range(0, n):
        element = int(input())
        list_of_numbers.append(element)
    num1 = list_of_numbers[0]
    num2 = list_of_numbers[1]
    gcd = find_gcd(num1, num2)
    for i in range(2, len(list_of_numbers)):
        gcd = find_gcd(gcd, list_of_numbers[i])
    print("ex1: The gcd is ", gcd)


def count_vowels(string):
    num_vowels = 0
    for char in string:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels + 1
    return num_vowels


def exercise2(word):
    """Prints how many vowels are in a word using count_vowels"""

    print("ex2: the number of vowels is ", count_vowels(word))


def exercise3(phrase, whole_string):
    """ Prints the number of occurrences of the phrase in a given string using count built-in function"""

    print("ex3: the number of occurrences the phrase is ", whole_string.count(phrase))


def change_case(given_set_of_words):
    res = [given_set_of_words[0].lower()]
    for c in given_set_of_words[1:]:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
    return ''.join(res)


def exercise4(phrase):
    """Converts from upper case to lower case with underscore using change_case"""

    print("ex4: changed case: ", change_case(phrase))


def exercise5(matrix):
    """
    Prints the matrix in spiral order
    four loops are used and each of the top,
    right, bottom and left corner of the matrix
    """

    print("ex5:")

    # base case
    if not matrix or not len(matrix):
        return

    top = left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    # print("the matrix length is: " + str(len(matrix)))

    while True:
        if left > right:
            break

        # output the top row
        for i in range(left, right + 1):
            print(matrix[top][i], end=' ')

        top = top + 1
        if top > bottom:
            break

        # output the right column
        for i in range(top, bottom + 1):
            print(matrix[i][right], end=' ')
        right = right - 1

        if left > right:
            break

        # output the bottom row
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=' ')
        bottom = bottom - 1

        if top > bottom:
            break

        # output the left column
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=' ')
        left = left + 1

    print("\n")


def exercise6():
    """
    Checks if the typed number is a palindrome
    """
    print("ex6:\n")
    n = int(input("Enter number:"))
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev:
        print("that's definitely a palindrome")
    else:
        print("no, the number isn't a palindrome!")


def exercise7(string):
    """
    Extracts the first number from the text
    d is a digit (a character in the range [0-9]), and +
    means one or more times.
    d+ means match one or more digits.
    search scans through string looking for the first location where the
    regular expression pattern produces a match
    .group() returns a tuple
    """

    number = re.search(r'\d+', string).group()
    print("ex7: the first number is ", number)


def hamming_weight(number):
    """Counts the occurrences of 1 in the str"""

    str_number = str(number)
    print("The binary of the number is ", str_number)
    one_count = 0
    for i in str_number:
        if i == "1":
            one_count += 1
    return one_count


def exercise8(number):
    """
    Calculates the number of occurrences of 1 in the binary
    representation of a number
    """

    print("ex8: the hamming weight is ", hamming_weight(str(bin(number))))


def exercise9(phrase):
    """Calculates the maximum occurrences of a letter in a phrase"""

    frequencies = {}
    for letter in phrase:
        letter = letter.lower()
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1

    maximum_integer = max(frequencies.values())
    for key in frequencies:
        if frequencies[key] == maximum_integer:
            print("ex9: the most frequent letter and its occurrence is: ", key, frequencies[key])


def exercise10(given_string):
    """Writes a function that counts how many words are present in a text"""

    list_of_words = given_string.split(" ")
    str_list = list(filter(None, list_of_words))
    print("ex10: the list of extracted words is --> ", str_list)
    print("the number of words is", len(str_list))


if __name__ == "__main__":
    
    exercise1()
    exercise2('This is my homework')
    exercise3('la', 'Pythonlalalalalalalanguage')
    exercise4('HelloMyNameIsDataScientist')
    given_matrix = [["1", "hei_rup", 3, 4, "python"],
                    [5, 6, 7, 8, "scripting"],
                    [9, 10, 11, 12, "hi_python_coding_from_another_world"],
                    [13, 14, 15, 16, "hello_coding2"]]
    exercise5(given_matrix)
    exercise6()
    exercise7('computersciencehas1000fieldsand100000000branchessoitshardtodo1thingbutilltry')
    exercise8(10)
    exercise9("HelloWoldCodeIsMyLifeNoLikeReally")
    exercise10("zen in python is a cool guide I would say")
    
