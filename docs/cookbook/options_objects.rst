Options objects
===============

Many WebPPL APIs have two broad styles:

1) Positional: ``fn(a, b, c)``
2) Options-first: ``fn({x: a, y: b, ...}, maybeOtherArgs...)``

Why use options objects?
------------------------

- Named arguments reduce ambiguity when there are many optional parameters.
- They make it clear which parameter you are setting.
- They allow stable extension without breaking call sites.

Practical rule of thumb
-----------------------

If the docs show ``{...}`` in the signature, treat it as *structural*:
you must pass an object with the right keys (e.g. ``data`` for ``mapData``),
not "some array that looks right".

Common bug pattern
------------------

Passing the raw array instead of ``{data: arr}`` usually fails or behaves oddly.
The fix is to wrap it in the required object shape.
