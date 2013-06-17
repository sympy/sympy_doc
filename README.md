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
of index.html remains intact. Do

    git reset -- dev/index.html

Then manually add in all the changes except the deletion of the index

    git add -p dev/index.html

(choose `patch`, `1`, choose `y` for all the changes except the deletion of
the different docs on the side.  The change will look something like


```diff
diff --git a/dev/index.html b/dev/index.html
index f4630b9..66bdfbf 100644
--- a/dev/index.html
+++ b/dev/index.html
@@ -187,14 +187,6 @@ report it</a>).</p>
             <p class="logo"><a href="#">
               <img class="logo" src="_static/sympylogo.png" alt="Logo"/>
             </a></p>
-            <h4>Docs for other versions</h4>
-            <p class="topless"><a href="../0.6.7/index.html">SymPy 0.6.7</a></p>
-            <p class="topless"><a href="../0.7.0/index.html">SymPy 0.7.0</a></p>
-            <p class="topless"><a href="../0.7.1/index.html">SymPy 0.7.1</a></p>
-            <p class="topless"><a href="../0.7.2/index.html">SymPy 0.7.2</a></p>
-            <p class="topless"><a href="../0.7.2-py3k/index.html">SymPy 0.7.2 (Python 3)</a></p>
-            <p class="topless"><a href="../dev/index.html">SymPy git</a></p>
-            <p class="topless"><a href="../dev-py3k/index.html">SymPy git (Python 3)</a></p>
   <h4>Next topic</h4>
   <p class="topless"><a href="install.html"
                         title="next chapter">Installation</a></p>
```

## Release docs

This is harder, because you have to update the index.  Checkout the SymPy
release tag and build the docs as above.  Then do

    cp -R ../path/to/sympy/doc/_build/html 0.7.3 # Replace 0.7.3 with the release number

Then, you have to edit all the `index.html` of all the docs that are there, to
add in

```html
<p class="topless"><a href="../0.7.3/index.html">SymPy 0.7.3</a></p>
```

(search the page for `Docs for other versions`).

You also need to add the whole thing to the docs you just added.  Open the
index pages to make sure you did it right.

Finally, you need to update the `latest` page. This is easy. Just run
`./generate_redirects.py 0.7.3 latest`, and commit the changes.

## Python 3

The Python 3 docs are done the same way as the regular docs. They are just
built from the Python 3 source.  Just do

    ./bin/use2to3

in the SymPy source first.  Note, you will need to install the Python 3
version of Sphinx to get the correct results (otherwise, it may include the
wrong version of the source code for the "show source" extension).  Copy the
docs here under the same name, only with `-py3k` appended.

## Pushing

Just push the branch up to GitHub.  The pages will be updated automatically.
If you don't have push access, fork this repo and make a pull request.

## Automation

If you want to write a script to automate some or all of this process, that
would be great.  Just send a pull request.  The script should probably go in
the SymPy repo, as part of the build script for the release process.
