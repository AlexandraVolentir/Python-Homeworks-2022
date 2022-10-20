"""
Homework 2 Python Programming 2022
19th of Oct 2022
© Volentir Alexandra, 3A5

The requirements can be found at: https://sites.google.com/site/fiipythonprogramming/laboratories/lab-2?authuser=0
"""

import collections


def recursive_fibonacci(n):
    """Recursive fibo"""

    if n == 0 or n == 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def exercise1(nr_of_terms):
    """Returns a list of the first n numbers
    in the fibo string"""

    fib_terms = list()
    if nr_of_terms <= 0:
        # print("The nr is not positive")
        pass
    else:
        # print("ex1:")
        for i in range(nr_of_terms):
            fib_terms.append(recursive_fibonacci(i))

    return fib_terms


def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def exercise2(list_of_numbers):
    """A function that receives a list of numbers and returns a list of the
    prime numbers found in it"""

    prime_numbers = list()
    for number in list_of_numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


def reunite_lists(list1, list2):
    final_list = sorted(list1 + list2)
    return list(dict.fromkeys(final_list))  # removes all duplicates


def intersect_lists(list1, list2):
    return [value for value in list1 if value in list2]


def exercise3(a, b):
    """Receives as parameters two lists a and b and returns:
    (a intersected with b, a reunited with b, a - b, b - a)"""

    map_of_lists = dict()
    map_of_lists['a intersected with b'] = intersect_lists(a, b)
    map_of_lists['a reunited with b'] = reunite_lists(a, b)
    map_of_lists['a - b'] = [item for item in b if item not in a]
    map_of_lists['b - a'] = [item for item in a if item not in b]
    return map_of_lists


def exercise4(list_of_musical_notes, list_of_integers, position):
    """receives as a parameters a list of musical notes (strings),
    a list of moves (integers) and a start position (integer).
    The function will return the song composed by going though the musical
    notes beginning with the start position and following the moves given as parameter."""

    final_melody = list()
    final_melody.append(list_of_musical_notes[position])
    last_position = position
    length = len(list_of_musical_notes)
    for integer in list_of_integers:
        final_melody.append(list_of_musical_notes[(last_position + integer) % length])
        last_position = last_position + integer
    return final_melody


def exercise5():
    """Receives as parameter a matrix and will return the matrix
    obtained by replacing all the elements under the main diagonal with 0 (zero)."""


def exercise6(n, *argv):
    for arg in argv:
        print(arg)

    pass


def exercise7(string):
    pass


def exercise8(number):
    pass


def exercise9(phrase):
    pass


def exercise10(given_string):
    pass


def check_list_duplicates(big_list, given_list):
    """checks if a list of lists already contains a list"""
    for my_list in big_list:
        if collections.Counter(my_list) == collections.Counter(given_list):
            return True
    return


def exercise11(list_of_tuples):
    """sorts a list of tuples based on the 3rd character of the 2nd element in a tuple"""

    list_of_tuples.sort(key=lambda b: b[1][2])
    return list_of_tuples


def exercise12(word_list):
    """Finds pairs of words with rhymes"""

    list_of_rhymes = list()
    for first_pair in word_list:
        for second_pair in word_list:
            new_list = list((first_pair, second_pair))
            if first_pair[-2:].strip().__eq__(second_pair[-2:].strip()) \
                    and first_pair != second_pair \
                    and not check_list_duplicates(list_of_rhymes, new_list):
                list_of_rhymes.append(new_list)
    return list_of_rhymes


if __name__ == "__main__":
    list_nr1 = [6, 8, 9, 10, 13, 17, 29, 31]
    list_nr2 = [6, 7, 8, 20]
    print("ex1: ", exercise1(8))
    print("ex2: ", exercise2(list_nr1))
    print("ex3: ", exercise3(list_nr1, list_nr2))
    print("ex4: ", exercise4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
    # print("ex6: ", exercise6())
    print("ex11:", exercise11(list([('abc', 'bcd'), ('abc', 'zza')])))
    print("ex12:", exercise12(list(("flower", "power", "ginger", "home", "pome"))))
