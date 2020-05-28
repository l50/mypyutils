import os

__auth__ = 'jayson.e.grace@gmail.com'


def file_exists(file):
    """Determine if a file at an input path exists or not.

    Args:
        file (str): The path to the file that we want to determine exists.

    Returns:
        bool: Return True if the file exists, False otherwise.

    Example:
        >>> from mypyutils import fileutils
        >>> fileutils.file_exists('/etc/passwd')
        True
        >>> fileutils.file_exists('/etc/passwdz')
        False
    """
    if os.path.isfile(file):
        return True
    else:
        return False


def file_to_list(file):
    """Return a list with the contents of an input file.

    Args:
        file (str): The path to the file that we want to turn into a list.

    Returns:
        list: The input file represented as a list.

    Example:
        >>> import os
        >>> os.system('echo "user1\nuser2\nuser3\nuser4\nuser5" > /tmp/test.txt')
        >>> from mypyutils import fileutils
        >>> fileutils.file_to_list('/tmp/test.txt')
        ['user1\n', 'user2\n', 'user3\n', 'user4\n', 'user5\n']
    """
    with open(file) as f:
        list = f.readlines()
        return list
