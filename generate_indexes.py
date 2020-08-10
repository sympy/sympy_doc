#!/usr/bin/env python

"""
Automatically generate "Docs for other versions".

"""

from __future__ import print_function

import codecs
import os
import os.path
import sys
import re

def main():
    dirs = ['latest', 'dev']
    # Simply update the releases list in each $RELEASEDIR/index.html.
    # This should be idempotent.
    versions = {}
    for releasedir in dirs:
        with codecs.open(os.path.join(releasedir, "index.html"), "r", "utf8") as f:
            lines = f.readlines()

        # Find the release version
        for line in lines:
            m = re.search(r"<title>Welcome to SymPy’s documentation! &#8212; SymPy (.*?) documentation</title>", line)
            if m:
                versions[releasedir] = m.group(1)
                break
        else:
            raise RuntimeError(f"Could not find the version for {releasedir}")

    releases = [('latest', f'SymPy {versions["latest"]} (latest release)'),
                ('dev', f'SymPy {versions["dev"]} (development version)')]

    for releasedir in dirs:
        with codecs.open(os.path.join(releasedir, "index.html"), "r", "utf8") as f:
            lines = f.readlines()

        # Find where in the file we need to edit
        context = [
            '<div class="sphinxsidebarwrapper">',
            '<p class="logo">',
            '<img class="logo" src="_static/sympylogo.png" alt="Logo"/>',
            '</a></p>'
        ]
        redirect = 'http-equiv="refresh"'
        contexti = 0
        for linei, line in enumerate(lines):
            # Did we match all we need to match?
            if contexti >= len(context):
                break
            # When we find a partial match, move to the next line to see if the
            # match continues. Otherwise, we start over.
            if context[contexti] in line:
                contexti += 1
            else:
                contexti = 0
        inserti = linei

        # If we didn't find a match in the whole file, we need to stop and fix something.
        if contexti < len(context):
            if any(redirect in line for line in lines):
                continue
            print("Couldn't find where to insert Docs for other versions in {0}".format(releasedir))
            sys.exit(0)

        # Do we want to delete anything? Is there a table there already?
        if "Documentation version" in lines[linei]:
            # Where does the current table end?
            # We want endi to be the first line not part of the current table.
            while linei < len(lines):
                linei += 1
                if 'p class="topless"' not in lines[linei]:
                    break
        endi = linei

        # Remove the current table and insert a new one.
        del lines[inserti:endi]
        for insertreleasedir, insertrelease in reversed(releases):
            if insertreleasedir == releasedir:
                lines.insert(inserti, '            <p class="topless">{0}</p>\n'.format(
                    insertrelease
                ))
            else:
                lines.insert(inserti, '            <p class="topless"><a href="../{0}/index.html">{1}</a></p>\n'.format(
                    insertreleasedir,
                    insertrelease
                ))
        lines.insert(inserti, "            <h4>Documentation version</h4>\n")

        # Write the changed file back out.
        with codecs.open(os.path.join(releasedir, "index.html"), "w", "utf8") as f:
            f.writelines(lines)


if __name__ == '__main__':
    sys.exit(main())
