Arrays vs tensors
=================

Arrays
------

Use arrays for:

- general-purpose lists,
- mapping/reducing,
- heterogeneous data (pairs, objects, strings, etc.).

Tensors
-------

Use tensors for:

- numeric computation where dimensionality matters,
- optimization/AD-heavy code,
- neural components and linear algebra.

Key gotcha: "flat storage"
--------------------------

When you build a tensor from a list, it is often **flat** + dims.
So for a 2x2 tensor you typically pass 4 values, not nested lists.

Example: ``Tensor([2, 2], [1, 2, 3, 4])``.
