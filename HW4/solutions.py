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


def write_absolute_paths(dir, name):
    """Ex2: Implementing a function so that in the file from the file path,
    the absolute path of each file inside the directory from
    the folder path, starting with the letter A, is written
    on one line."""

    if not is_directory(dir) or not is_file(name):
        return path_err

    with open(name, 'w') as file:
        for (root, directories, files) in os.walk(dir):
            for file_name in files:
                if file_name[0] == 'A':
                    abs_path = os.path.join(os.path.abspath(root), file_name)
                    file.write(abs_path + '\n')
    return "Check up the output/ex2.txt file"


def get_last_20_chars(name):
    """Get the last 20 characters from the contents of a file"""

    with open(name, 'r') as file:
        filesize = os.path.getsize(name)
        if filesize > 20:
            file.seek(filesize - 20)
        return file.read()


def get_file_extension_freq(dir):
    """Returns the file extension frequency"""

    freq = {}
    for (root, directories, files) in os.walk(dir):
        for name in files:
            ext = os.path.splitext(name)[1][1:]
            if ext != '':
                freq[ext] = freq.get(ext, 0) + 1
    return sorted([(k, v) for k, v in freq.items()], key=lambda elem: elem[1], reverse=True)


def get_by_path(path):
    """Ex3: Implements the functions get_file_extension_frequency
    and get_last_20_chars"""

    if os.path.isfile(path):
        return get_last_20_chars(path)
    if os.path.isdir(path):
        return get_file_extension_freq(path)


def get_list_of_sorted_extensions_cmd(dir):
    """Ex4: Returns a list of unique extensions
    from the dir given argument """

    if not is_directory(dir):
        return path_err

    return sorted(
        [ext for ext in {os.path.splitext(file)[1][1:] for file in os.listdir(os.path.abspath(dir))}
         if ext != '']) if os.path.exists(dir) else not_found_err


def file_search_ex5(targ, look_up):
    """Ex5: Returns a list of files that contain to_search"""

    if not is_file(targ) and not is_directory(targ) and not is_string(look_up):
        return "Wrong parameters"

    try:
        if os.path.isfile(targ):
            if if_contains_elm(targ, look_up):
                return [targ]

        elif os.path.isdir(targ):
            files_with_look_up = []
            for (root, directories, files) in os.walk(targ):
                for name_file in files:
                    file_path = os.path.join(root, name_file)
                    if if_contains_elm(file_path, look_up):
                        files_with_look_up.append(file_path)
            return files_with_look_up
        else:
            raise ValueError(targ + ' is not a file/directory')
    except ValueError as e:
        print(e)


def if_contains_elm(name, look_up):
    with open(name, 'r') as file:
        return look_up in file.read()


def file_search_ex6(targ, to_search, callback):
    """Ex6: similar to ex5, but receives a callback func"""

    if not is_file(targ) and not is_directory(targ) and not is_string(to_search):
        return "Wrong parameters"

    try:
        if os.path.isfile(targ):
            if if_contains_elm(targ, to_search):
                return [targ]

        if os.path.isdir(targ):
            files_containing_elm = []
            for (root, directories, files) in os.walk(targ):
                for file_name in files:
                    path = os.path.join(root, file_name)
                    if if_contains_elm(path, to_search):
                        files_containing_elm.append(path)
            return files_containing_elm

        raise ValueError(targ + ' is not a file/directory')
    except ValueError as e:
        callback(e)


def get_info(path):
    """Ex7: Returns a specific dictionary

    characterising the path given as parameter"""
    return {
        'full_path': os.path.abspath(path),
        'file_size': os.path.getsize(path),
        'file_extension': os.path.splitext(path)[1][1:],
        'can_read': os.access(path, os.R_OK),
        'can_write': os.access(path, os.W_OK)
    } if os.path.exists(path) else not_found_err


def get_all_absolute_paths(path):
    """Ex8: Returns a list of all the absolute paths of the files
    that are located at the root of the dir_path"""

    if not is_directory(path):
        return path_err

    return [os.path.join(os.path.abspath(path), file) for file in
            os.listdir(os.path.abspath(path)) if os.path.isfile(os.path.join(path, file))] \
        if os.path.isdir(path) else not_found_err
