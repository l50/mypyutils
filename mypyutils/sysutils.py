def chomp(x):
    """ Simulate perl's chomp.

    """
    if x.endswith("\r\n"):
        return x[:-2]
    if x.endswith("\n") or x.endswith("\r"):
        return x[:-1]
    return x


def run_cmd(cmd):
    """ Used to run a system command specified with the cmd parameter and return its output.

    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return output
