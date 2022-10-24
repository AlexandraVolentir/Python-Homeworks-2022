import inspect

from input_verification_functions import *
from collections import Counter


def get_reunited_sets(set1, set2):
    return set1.union(set2)


def get_intersected_sets(set1, set2):
    return set1.intersection(set2)


def get_set_from_reunited_lists(list1, list2):
    return set(list1).union(set(list2))


def get_set_from_intersected_lists(list1, list2):
    return set(list1).intersection(set(list2))


def exercise1(a, b):
    """
    Calculates the intersection, reunion,
    and difference between the 2 lists passed as arguments
    :param a: the first list
    :param b: the second list
    :return: a list of sets containing a intersected with b,
    a reunited with b, a - b, b - a
    """
    if (not check_integer_list(a)) \
            or not check_integer_list(b):
        return "Invalid lists"

    list_of_sets = list()
    list_of_sets.append(get_set_from_intersected_lists(a, b))
    list_of_sets.append(get_set_from_reunited_lists(a, b))
    list_of_sets.append(set(a) - set(b))
    list_of_sets.append(set(b) - set(a))
    return list_of_sets


def exercise2(string):
    """
    Calculates the frequency of characters in a string
    *Count* collection counts elements from an input iterable
    :param string: a string
    :return: a dictionary with the character frequency
    """
    if not is_string(string):
        return "Invalid input"
    res = dict(Counter(string))
    return res


def exercise3(d1, d2):
    """
    Compares two dictionaries without using "=="
    DeepDiff recursively compares the dictionaries
    :param d1: first dictionary
    :param d2: second dictionary
    :return: the result of the recursive comparison
    """

    if not is_dict(d1) or not is_dict(d2):
        return "Invalid input"
    from deepdiff import DeepDiff
    return len(DeepDiff(d1, d2)) == 0


def build_xml_element(tag, content, href, _class, id):
    # TODO how to elegantly make this
    # key_values_concatenated = ','.join(key_value)
    # print(key_values_concatenated)
    pass


def exercise4(tag, content, href, _class, id):
    return build_xml_element(tag, content, href, _class, id)


def check_input_dict_validator(validation_rules, dictionary):
    if not is_set(validation_rules) or not is_dict(dictionary):
        return False

    for rule in validation_rules:
        if len(rule) != 4:
            return False
    return True


def validate_dict(validation_rules, dictionary):
    """
    Checks if the dictionary satisfies the given rules
    :param validation_rules: a set of tuples
    :param dictionary: the dictionary
    :return: True if matches all the rules, False otherwise
    """
    if not check_input_dict_validator(validation_rules, dictionary):
        return "Invalid input"

    for rule in validation_rules:
        value = dictionary.get(rule[0])

        if value is None:
            return False

        if not value.startswith(rule[1]) or not value.__contains__(
                rule[2]) or not value.endswith(rule[3]):
            return False
    return True


def exercise5(validation_rules, dictionary):
    return validate_dict(validation_rules, dictionary)


def get_unique_elements(list_given):
    visited = set()
    unique = []
    for elm in list_given:
        if elm not in visited:
            unique.append(elm)
            visited.add(elm)
    return unique


def exercise6(list_of_elm):
    """
    Calculates unique and duplicates in a list
    intersection_update() - removes the unwanted items from the original set
    intersection() - returns a new set, with the duplicates
    :param list_of_elm: a list
    :return: a tuple (a,b), where a represents the nr of unique elements in the list
    and b the duplicate elm
    """
    if not check_integer_list(list_of_elm):
        return "Invalid input"
    # TODO
    unique_elm = set(list_of_elm)
    # duplicates =

    return unique_elm


def exercise7(*sets):
    """
    Calculates intersection, reunion and difference for all given sets 2 by 2
    :param sets: a variable number of sets
    :return: a dictionary with |, &, - from all sets 2 by 2
    """

    for singular_set in sets:
        if not is_set(singular_set):
            return "Invalid input"

    # TODO verify if there are any duplicates
    result = dict()
    list_of_sets = list()
    for singular_set in sets:
        list_of_sets.append(singular_set)
    verified_sets = list()
    for set_elm1 in list_of_sets:
        for set_elm2 in list_of_sets:
            if set_elm1 != set_elm2:
                result[str(set_elm1) + ' | ' + str(set_elm2)] = get_reunited_sets(set_elm1, set_elm2)
                result[str(set_elm1) + ' & ' + str(set_elm2)] = get_intersected_sets(set_elm1, set_elm2)
                result[str(set_elm1) + ' - ' + str(set_elm2)] = set_elm1 - set_elm2
                result[str(set_elm2) + ' - ' + str(set_elm1)] = set_elm2 - set_elm1
    return result


def exercise8(mapping):
    """
    Iterate through a map where the
    value of the current key is the key for the next value
    until we find a loop
    :param mapping: a dictionary
    :return: a list of objects obtained
    """

    if not is_dict(mapping):
        return "Invalid input"

    visited_keys = list()
    cur_value = "start"
    while cur_value not in visited_keys:
        if cur_value in mapping:
            visited_keys.append(cur_value)
            cur_value = mapping[cur_value]
        else:
            break
    return visited_keys


def count_positional_args(func):
    """Counts the positional arguments from the signature of the function"""

    sign = inspect.signature(func)
    empty = inspect.Parameter.empty
    counter = 0
    for parameter in sign.parameters.values():
        if parameter.default is empty:
            counter += 1
    return counter


def exercise9(a, b, c, d, x=1, y=2, z=3, w=5):
    """
    Calculates the number of positional arguments
    whose values can be found among keyword arguments values
    The locals() method returns a dictionary with
    all the local variables
    :return: integer with nr of matching values
    """
    # TODO variable number of positional and keyword arguments
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

