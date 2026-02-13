project = 'WebPPL Reference Manual (Executable Examples)'
copyright = '2026'
author = 'WebPPL contributors (refman template)'

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'myst_parser',
    'sphinxcontrib.programoutput',
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
autosectionlabel_prefix_document = True

html_static_path = ['_static']

html_baseurl = "https://mozow01.github.io/WebpplHelp/"
