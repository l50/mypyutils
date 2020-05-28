import subprocess

__auth__ = 'jayson.e.grace@gmail.com'

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
    return output.decode('utf-8').strip()
