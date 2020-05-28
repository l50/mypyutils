import subprocess

__auth__ = 'jayson.e.grace@gmail.com'

def chomp(input):
    """Remove any trailing newline or carriage return characters in an input string.

    Args:
        input (str): The string that we want to chomp.

    Returns:
        string: Modified input string with no trailing \n or \r.

    Example:
        >>> from mypyutils import sysutils
        >>> sysutils.chomp('blablabla\r\n')
        'blablabla'
    
    .. _Original Resource:
       https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
    """
    if input.endswith("\r\n"):
        return input[:-2]
    if input.endswith("\n") or input.endswith("\r"):
        return input[:-1]
    return input


def run_cmd(cmd):
    """Used to run a system command specified with the cmd parameter and return its output.

    Args:
        cmd (str): The command we want to run.

    Returns:
        string: The output from running the specified command.

    Example:
        >>> from mypyutils import sysutils
        >>> sysutils.run_cmd('uname')
        'Darwin'
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return chomp(output.decode('utf-8'))
