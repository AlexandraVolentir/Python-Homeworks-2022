"""
Homework 3 Python Programming 2022
23rd of Oct 2022
Ⓒ Volentir Alexandra, 3A5

The requirements can be found at: https://sites.google.com/site/fiipythonprogramming/laboratories/lab-3?authuser=0
"""

from solutions import *


def test_func():
    list_nr1 = [6, 8, 9, 10, 13, 17, 29, 31]
    list_nr2 = [6, 7, 8, 20]
    print("ex1: ", exercise1(list_nr1, list_nr2))
    print("ex2: ", exercise2("Ana has apples."))
    print("ex3: ")
    print("ex4: ")
    print("ex5: ")
    print("ex6: ")
    print("ex7: ")
    operation_dict = exercise7({1, 2}, {2, 3})
    for operation in operation_dict:
        print(operation, ": ", operation_dict[operation])
    print("ex8: ", exercise8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
    print("ex9: number of common values in pos and var arguments is ---> ", exercise9(1, 2, 3, 4, x=1, y=2, z=3, w=5))











if __name__ == "__main__":
    test_func()