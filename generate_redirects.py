#!/usr/bin/env python

"""
Automatically generate redirect pages.

"""

import os
import sys
import argparse
import shutil

REDIRECT_TEMPLATE = """\
<html>
    <head>
        <meta http-equiv="refresh" content="0;URL={}" />
    </head>
    <body>
    </body>
</html>

"""

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "source",
        action="store",
        nargs=1,
        )
    p.add_argument(
        "dest",
        action="store",
        nargs=1,
        )
    args = p.parse_args()

    source = args.source[0].rstrip('/')
    dest = args.dest[0].rstrip('/')

    if os.path.exists(dest):
        shutil.rmtree(dest)

    for dirpath, dirnames, filenames in os.walk(source):
        newpath = os.path.join(dest, *dirpath.split(os.path.sep)[1:])
        os.makedirs(newpath)

        for file in filenames:
            # It must always be /, even on Windows
            redirect = '/'.join(['', source] + dirpath.split(os.path.sep)[1:] + [file])
            with open(os.path.join(newpath, file), 'w') as f:
                f.write(REDIRECT_TEMPLATE.format(redirect))

if __name__ == '__main__':
    sys.exit(main())
