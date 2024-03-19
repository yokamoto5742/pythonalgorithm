import sys


def py2_or_py3():
    """Prints the version of Python you are using.

    This function uses the sys module to determine the version of Python
    you are using. It then prints a message to the console.
    """

    major = sys.version_info.major
    if major == 2:
        print('You are using Python 2.')
    elif major == 3:
        print('You are using Python 3.')
    else:
        print('You are using an unknown version of Python.')


if __name__ == '__main__':
    py2_or_py3()
