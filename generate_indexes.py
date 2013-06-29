#!/usr/bin/env python

"""
Automatically generate "Docs for other versions".

"""

import codecs
import os
import os.path
import sys
import shutil


def main():
    # Get a list of all the releases, in order.
    # These are held in a file, releases.txt where
    # each line includes RELEASEDIR:Release Name.
    releases = []
    with codecs.open("releases.txt", "r", "utf8") as f:
        for linei, line in enumerate(f):
            parts = line.strip().split(":")
            if len(parts) != 2:
                print "Error parsing line {0}".format(linei)
                sys.exit(1)
            releases.append((parts[0], parts[1]))

    # Simply update the releases list in each $RELEASEDIR/index.html.
    # This should be idempotent.
    for releasedir, releasename in releases:
        with codecs.open(os.path.join(releasedir, "index.html"), "r", "utf8") as f:
            lines = f.readlines()

        # Find where in the file we need to edit
        context = [
            '<div class="sphinxsidebarwrapper">',
            '<p class="logo">',
            '<img class="logo" src="_static/sympylogo.png" alt="Logo"/>',
            '</a></p>'
        ]

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
            print "Couldn't find where to insert Docs for other versions in {0}".format(releasedir)
            sys.exit(2)

        # Do we want to delete anything? Is there a table there already?
        if "Docs for other versions" in lines[linei]:
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
            lines.insert(inserti, '            <p class="topless"><a href="../{0}/index.html">{1}</a></p>\n'.format(
                insertreleasedir,
                insertrelease
            ))
        lines.insert(inserti, "            <h4>Docs for other versions</h4>\n")

        # Write the changed file back out.
        with codecs.open(os.path.join(releasedir, "index.html"), "w", "utf8") as f:
            f.writelines(lines)


if __name__ == '__main__':
    sys.exit(main())
