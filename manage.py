#!/usr/bin/env python
import os
import sys
import glob

if __name__ == "__main__":
    if 'test' in sys.argv:
        env_dir = os.path.join('tests', 'env')
    else:
        env_dir = 'env'
    env_vars = glob.glob(os.path.join(env_dir, '*'))
    for env_var in env_vars:
        with open(env_var, 'r') as env_var_file:
            os.environ.setdefault(env_var.split(os.sep)[-1],
                                  env_var_file.read().strip())

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
