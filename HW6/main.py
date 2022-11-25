
from solutions import *

if __name__ == "__main__":
    print("ex1: ", exercise1("keep it super simple"))
    print("ex2: ", exercise2(r"\w+", "text, ora a sosit", 3))
    print("ex3: ", exercise3("keep it super simple", [r"\w+", r"simple"]))
    print("ex4: ", exercise4("file.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
    print("ex5", exercise5("file.xml", {"class": "url", "name": "url-form", "data-id": "item"}))
    print("ex6: ", exercise6("ala cere ora"))
    print(exercise7(""))
    exercise8(".", "main.*")
