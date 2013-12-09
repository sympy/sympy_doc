# SymPy Docs Repository

This git repository contains all the generated SymPy documentation. It is
hosted at http://docs.sympy.org/ automatically by github.

To build the docs in SymPy, cd into the SymPy clone, and do

    cd doc
    make clean
    make html

Then the built docs are in `_build/html`.  To update the docs here, there are
several things.

## Development docs

These are the easiest.  Just build the docs from the latest SymPy master.
Then, do

    rm -rf dev/
    cp -R ../path/to/sympy/doc/_build/html dev/

Then

    git add -A dev/

Finally, you need to make sure the index of the different docs on the the left
of index.html remains intact. Run

    ./generate_indices.py

## Release docs

This is harder, because you have to update the index.

First, move the current latest docs to the version number (which should
currently be a redirect to the `latest` docs).

    git rm -r 0.7.2/
    git mv latest 0.7.3

Checkout the SymPy release tag and build the docs as above.  Then do

    cp -R ../path/to/sympy/doc/_build/html 0.7.3

Edit `releases.txt` with the new release. Then run

    ./generate_indices.py

Finally, you need to make sure the url with the latest version redirects to
`latest`. This is easy. Just run `./generate_redirects.py 0.7.3 latest`, and
commit the changes.

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
