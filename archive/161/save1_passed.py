import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    contents = list(os.walk(directory, topdown=True))
    return len(contents)-1, sum(len(item[2]) for item in contents)
