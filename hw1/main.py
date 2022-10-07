import collections
import re


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


# find the gcd of multiple numbers read from the console
def exercise1():
    lst = []
    n = int(input("Enter number of elements : "))
    if n < 2:
        n = 2
    for i in range(0, n):
        element = int(input())
        lst.append(element)
    num1 = lst[0]
    num2 = lst[1]
    gcd = find_gcd(num1, num2)
    for i in range(2, len(lst)):
        gcd = find_gcd(gcd, lst[i])
    print(gcd)


def count_vowels(string):
    num_vowels = 0
    for char in string:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels + 1
    return num_vowels


# calculates how many vowels are in a word
def exercise2(word):
    print(count_vowels(word))


# write a script that receives two strings
# n prints the number of occurrences of the first str in the sec
def exercise3(whole_string, phrase):
    print(whole_string.count(phrase))


def change_case(given_set_of_words):
    res = [given_set_of_words[0].lower()]
    for c in given_set_of_words[1:]:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
    return ''.join(res)


# convert from upper case to lower case with underscore
def exercise4(phrase):
    print(change_case(phrase))


# print the matrix in spiral order
def exercise5(matrix):
    ans = []
    if len(matrix) == 0:
        return ans

    m = len(matrix)
    n = len(matrix[0])
    seen = [[0 for i in range(n)] for j in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    x = 0
    y = 0
    di = 0

    # Iterate from 0 to R * C - 1
    for i in range(m * n):
        ans.append(matrix[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]

        if 0 <= cr < m and 0 <= cc < n and not (seen[cr][cc]):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return ans


# Check if the number is a polindrome
def exercise6():
    n = int(input("Enter number:"))
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    if temp == rev:
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")


# \d is a digit (a character in the range [0-9]), and +
# means one or more times. Thus, \d+ means match one or more digits.
def exercise7(string):
    number = re.search(r'\d+', string).group()
    print(number)


def hamming_weight(n):
    n = str(n)
    print(n)
    one_count = 0
    for i in n:
     if i == "1":
        one_count += 1
    print(one_count)


# calc the number of occurrences of 1 in binary
def exercise8(n):
    return hamming_weight(str(bin(n)))


def exercise9(phrase):
    all_freq = {}
    for letter in phrase:
        letter = letter.lower()
        if letter in all_freq:
            all_freq[letter] += 1
        else:
            all_freq[letter] = 1

    maximum_integer = max(all_freq.values())
    for key in all_freq:
        if all_freq[key] == maximum_integer:
            return key, all_freq[key]


def exercise10(given_string):
    list_of_words = given_string.split(" ")
    str_list = list(filter(None, list_of_words))
    print(str_list)


if __name__ == "__main__":
    # exercise1()
    exercise2('hello agaaaaaain')
    exercise3('hiiiiiiioioioioioioioi', 'oi')
    exercise4('HelloMyNameIsJohn')
    exercise7('hiiiiiii565656hihihi8999')
    a = [["1", "hei rup", 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

    # Function call
    for x in exercise5(a):
        print(x, end=" ")
    print()
    exercise8(2000)
    print(exercise9("HellooooMyyFrieeeend"))
    exercise10("hei hei salut")
