# Contributing

## Add a new documented example

1. Put runnable WebPPL code in `examples/.../*.wppl`
2. Reference it from a `.rst` page using both directives:

```rst
.. literalinclude:: ../examples/path/to/example.wppl
   :language: javascript
   :linenos:

.. program-output:: python ../scripts/run_webppl.py ../examples/path/to/example.wppl --random-seed 0
   :prompt:
   :ellipsis: 0
```

3. Run checks:

```bash
npm run test:examples
sphinx-build -b html docs _build/html
```
