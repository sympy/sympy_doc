# SymPy Docs Repository

**NOTE: The contents of this repository are generated automatically. To make
modifications to the SymPy documentation, edit the RST sources in the `doc`
directory of the [main SymPy
repo](https://github.com/sympy/sympy/tree/master/doc). Pull requests should
only be made to this repo if you are modifying old version builds of the docs,
or for emergency hotfixes.**

This git repository contains all the generated SymPy documentation. It is
hosted at http://docs.sympy.org/ automatically by github.

To build the docs in SymPy, cd into the SymPy clone, and do

    cd doc
    make clean
    make html

Then the built docs are in `_build/html`.  To update the docs here, there are
several things.

## Development docs

**NOTE: The doctr command that runs on Travis on the sympy/sympy repo does
this automatically. There is usually not a need to do this manually.**

Build the docs from the latest SymPy master. Then, do

    rm -rf dev/
    cp -R ../path/to/sympy/doc/_build/html dev/

Then

    git add -A dev/

Finally, you need to make sure the index of the different docs on the left
of index.html remains intact. Run

    ./generate_indexes.py

## Release docs

**NOTE: This should be done automatically by the SymPy release script. It
should only be done manually if the release script doesn't do it correctly for
some reason.**

First, completely remove the old release docs

    git rm -rf latest/

Checkout the SymPy release tag and build the docs as above.  Then do
a
    cp -R ../path/to/sympy/doc/_build/html latest/

Then run

    ./generate_indexes.py

And add the results

    git add -A dev/ latest/ releases.txt

## Making redirects

The `generate_redirects.py` script can generate redirects from one path to
another.

We used to host old versions of the docs on this, but now we only host the
latest and development docs. The old docs that were there have redirects to
the latest docs. This is only done so that old links can continue to work. It
is not necessary to add redirects for future versions.

## Pull requests

If you are making a significant change to the documentation in a pull request,
feel free to use this site to upload a live version of it.  Just create a
directory with a reasonable name and put your docs there. If you share the
link with a lot of people before the pull request is merged, you might want to
sue the `generate_redirects.py` script to convert the special directory into a
redirect to `dev` once the pull request is merged.

## Pushing

Just push the branch up to GitHub.  The pages will be updated automatically.
If you don't have push access, fork this repo and make a pull request.

## Automation

If you want to write a script to automate some or all of this process, that
would be great.  Just send a pull request.  The script should probably go in
the SymPy repo, as part of the build script for the release process.
