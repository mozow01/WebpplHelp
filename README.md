# WebPPL refman with executable examples

## Install dependencies

You need Python + Node.js.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

npm install
```

## Run all examples (CI-style)

```bash
npm run test:examples
```

## Build HTML docs

```bash
sphinx-build -b html docs _build/html
```

If `webppl` is installed (via `npm install` above), the docs build will execute
example programs and embed their output.

## Determinism

Examples are run with `--random-seed 0` unless an example explicitly chooses another seed.
