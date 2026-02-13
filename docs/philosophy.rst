Philosophy: docs that don't lie
==============================

The goal is to avoid "móricka-style" one-liners and instead provide:

- Exact call forms (positional vs options-object).
- Precise data shapes (e.g. arrays vs tensors vs objects).
- Working examples, including *what to run* and *what to expect*.

How we keep examples working
----------------------------

Examples live under ``examples/`` as real ``.wppl`` files.

The Sphinx build can **execute** them and embed their output using
``sphinxcontrib-programoutput``.

If you don't want to execute examples while building docs, you can still run
them in CI via:

``npm run test:examples``

Determinism
-----------

When a snippet uses randomness, we run it with a fixed seed (``--random-seed``)
so the output is reproducible.
