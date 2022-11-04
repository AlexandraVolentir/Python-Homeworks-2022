import os

not_found_err = "The dictionary was not found"
path_err = "Path specified invalid"


def is_file(path):
    return os.path.isfile(path)


def is_directory(path):
    return os.path.isdir(path)


def is_string(str1):
    if not isinstance(str1, str):
        return False
    return True


def get_list_of_sorted_extensions(directory):
    """
    Ex1: Returns a list of unique extensions sorted
    increasingly (alphabetically) from the directory given
    as parameter
    """
    if not is_directory(directory):
        return path_err

    return sorted(
        [ext for ext in {os.path.splitext(file)[1][1:] for file in os.listdir(os.path.abspath(directory))}
         if ext != '']) if os.path.exists(directory) else not_found_err


def write_absolute_paths(directory, filename):
    """Ex2: Implementing a function so that in the file from the file path,
    the absolute path of each file inside the directory from
    the folder path, starting with the letter A, is written
    on one line."""

    if not is_directory(directory) or not is_file(filename):
        return path_err

    with open(filename, 'w') as file:
        for (root, directories, files) in os.walk(directory):
            for file_name in files:
                if file_name[0] == 'A':
                    absolute_path = os.path.join(os.path.abspath(root), file_name)
                    file.write(absolute_path + '\n')
    return "Check up the output/ex2.txt file"


def get_last_20_chars(filename):
    """Get the last 20 characters from the contents of a file"""

    with open(filename, 'r') as file:
        filesize = os.path.getsize(filename)
        if filesize > 20:
            file.seek(filesize - 20)
        return file.read()


def get_file_extension_freq(directory):
    """Returns the file extension frequency"""

    frequency = {}
    for (root, directories, files) in os.walk(directory):
        for filename in files:
            extension = os.path.splitext(filename)[1][1:]
            if extension != '':
                frequency[extension] = frequency.get(extension, 0) + 1
    return sorted([(key, value) for key, value in frequency.items()], key=lambda elem: elem[1], reverse=True)


def get_by_path(my_path):
    """Ex3: Implements the functions get_file_extension_frequency
    and get_last_20_chars"""

    if os.path.isfile(my_path):
        return get_last_20_chars(my_path)
    if os.path.isdir(my_path):
        return get_file_extension_freq(my_path)


def get_list_of_sorted_extensions_cmd(directory):
    """Ex4: Returns a list of unique extensions
    from the dir given argument """

    if not is_directory(directory):
        return path_err

    return sorted(
        [extension for extension in {os.path.splitext(file)[1][1:] for file in os.listdir(os.path.abspath(directory))}
         if extension != '']) if os.path.exists(directory) else not_found_err


def file_search_ex5(targ, to_search):
    """Ex5: Returns a list of files that contain to_search"""

    if not is_file(targ) and not is_directory(targ) and not is_string(to_search):
        return "Wrong parameters"

    try:
        if os.path.isfile(targ):
            if check_if_file_contains_to_search(targ, to_search):
                return [targ]

        elif os.path.isdir(targ):
            files_with_to_search = []
            for (root, directories, files) in os.walk(targ):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    if check_if_file_contains_to_search(file_path, to_search):
                        files_with_to_search.append(file_path)
            return files_with_to_search
        else:
            raise ValueError(targ + ' is not a file/directory')
    except ValueError as e:
        print(e)


def check_if_file_contains_to_search(filename, to_search):
    with open(filename, 'r') as file:
        return to_search in file.read()


def file_search_ex6(targ, to_search, callback):
    """Ex6: similar to ex5, but receives a callback func"""

    if not is_file(targ) and not is_directory(targ) and not is_string(to_search):
        return "Wrong parameters"

    try:
        if os.path.isfile(targ):
            if check_if_file_contains_to_search(targ, to_search):
                return [targ]

        if os.path.isdir(targ):
            files_with_to_search = []
            for (root, directories, files) in os.walk(targ):
                for file_name in files:
                    path = os.path.join(root, file_name)
                    if check_if_file_contains_to_search(path, to_search):
                        files_with_to_search.append(path)
            return files_with_to_search

        raise ValueError(targ + ' is not a file/directory')
    except ValueError as e:
        callback(e)


def get_info(file_path):
    """Ex7: Returns a specific dictionary

    characterising the path given as parameter"""
    return {
        'full_path': os.path.abspath(file_path),
        'file_size': os.path.getsize(file_path),
        'file_extension': os.path.splitext(file_path)[1][1:],
        'can_read': os.access(file_path, os.R_OK),
        'can_write': os.access(file_path, os.W_OK)
    } if os.path.exists(file_path) else not_found_err


def get_all_absolute_paths(dir_path):
    """Ex8: Returns a list of all the absolute paths of the files
    that are located at the root of the dir_path"""

    if not is_directory(dir_path):
        return path_err

    return [os.path.join(os.path.abspath(dir_path), file) for file in
            os.listdir(os.path.abspath(dir_path)) if os.path.isfile(os.path.join(dir_path, file))] \
        if os.path.isdir(dir_path) else not_found_err
