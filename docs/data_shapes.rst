Data shapes and call forms
=========================

This chapter exists specifically for the most common WebPPL pain point:
*"I passed a list in the wrong shape and the docs didn't tell me."*

Arrays (a.k.a. "lists")
-----------------------

In WebPPL, the usual "list" is a JavaScript-style array literal: ``[a, b, c]``.

Example: ``map(fn, arr)``

.. literalinclude:: ../examples/arrays/map.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/arrays/map.wppl --random-seed 0

Options objects (named arguments)
---------------------------------

Some functions use an **options object** as their first argument. That is a
JavaScript object literal: ``{key: value, ...}``.

Example: ``mapData({data: arr[, batchSize: n]}, fn)``

.. literalinclude:: ../examples/arrays/mapData.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/arrays/mapData.wppl --random-seed 0

Tensors: dims + flat array
--------------------------

Tensor constructors often take:

- ``dims``: an array of dimension sizes (e.g. ``[2, 2, 2]``)
- ``arr``: a **flat** array of values

Example: ``Tensor(dims, arr)``

.. literalinclude:: ../examples/tensors/tensor.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/tensors/tensor.wppl --random-seed 0

Inference call form (always options object)
-------------------------------------------

Inference is typically invoked via an options object:

``Infer({method: 'enumerate', model: model})``

.. literalinclude:: ../examples/inference/enumerate.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py examples/inference/enumerate.wppl --random-seed 0

