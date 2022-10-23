import inspect

from input_verification_functions import *
from collections import Counter


def get_reunited_sets(set1, set2):
    return set1.union(set2)


def get_intersected_sets(set1, set2):
    return set1.intersection(set2)


def get_reunited_lists(list1, list2):
    return set(list1).union(set(list2))


def get_intersected_lists(list1, list2):
    return set(list1).intersection(set(list2))


def exercise1(a, b):
    if (not check_integer_list(a)) \
            or not check_integer_list(b):
        return "Invalid lists"

    list_of_sets = list()
    list_of_sets.append(get_intersected_lists(a, b))
    list_of_sets.append(get_reunited_lists(a, b))
    list_of_sets.append(set(a) - set(b))
    list_of_sets.append(set(b) - set(a))
    return list_of_sets


def exercise2(word):
    """
    Counter
    :param word:
    :return:
    """
    res = dict(Counter(word))
    return res


def exercise3(phrase, whole_string):
    pass


def exercise4(phrase):
    pass


def exercise5(matrix):
    pass


def exercise6():
    pass


def exercise7(*sets):
    # TODO verify if there are any duplicates
    result = dict()
    list_of_sets = list()
    for singular_set in sets:
        list_of_sets.append(singular_set)
    verified_sets = list()
    for set_elm in list_of_sets:
        for set_elm2 in list_of_sets:
            if set_elm != set_elm2:
                result[str(set_elm) + ' | ' + str(set_elm2)] = get_reunited_sets(set_elm, set_elm2)
                result[str(set_elm) + ' & ' + str(set_elm2)] = get_intersected_sets(set_elm, set_elm2)
                result[str(set_elm) + ' - ' + str(set_elm2)] = set_elm - set_elm2
                result[str(set_elm2) + ' - ' + str(set_elm)] = set_elm2 - set_elm

    return result


def exercise8(dictionary):
    visited_keys = list()
    cur_value = "start"
    while cur_value not in visited_keys:
        if cur_value in dictionary:
            visited_keys.append(cur_value)
            cur_value = dictionary[cur_value]
        else:
            break
    return visited_keys


def count_positional_args(func):
    sign = inspect.signature(func)
    empty = inspect.Parameter.empty
    counter = 0
    for parameter in sign.parameters.values():
        if parameter.default is empty:
            counter += 1
    return counter


def exercise9(a, b, c, d, x=1, y=2, z=3, w=5):
    """
    The locals() method returns a dictionary with
    all the local variables and symbols for the current function at the moment,
    so we will save it at the beginning
    """

    saved_args = locals()
    pos_arg_counter = count_positional_args(exercise9)
    pos_arg = set()
    var_arg = set()
    counter = 0
    for elm in saved_args:
        if counter < pos_arg_counter:
            pos_arg.add(saved_args[elm])
        else:
            var_arg.add(saved_args[elm])
        counter += 1
    return len(pos_arg.intersection(var_arg))

