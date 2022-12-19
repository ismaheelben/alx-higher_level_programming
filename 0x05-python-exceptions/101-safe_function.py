#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as zero_err:
        sys.stderr.write("Exception: {}\n".format(zero_err))
    except IndexError as idx_err:
        sys.stderr.write("Exception: {}\n".format(idx_err))
