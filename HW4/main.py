"""
Homework 4 Python Programming 2022
1st of November 2022
:copyright: Volentir Alexandra, 3A5

The requirements can be found at: https://sites.google.com/site/fiipythonprogramming/laboratories/lab-4?authuser=0
"""

from solutions import *


def test_func():
    directory = "sample_dir"
    print("ex1: ", get_extensions(directory))
    print("ex2: ", write_abs_paths(directory, "output/ex2.txt"))
    print("ex3: ", get_by_path("sample_dir/data.csv"))
    print("ex4: ", get_extensions(directory))
    print("ex5: ", file_lookup_ex5("sample_dir/file.txt", "swing"))
    print("ex7: ", get_data("sample_dir/file.txt"))
    print("ex8: ", get_all_absolute_paths(directory))


if __name__ == "__main__":
    test_func()