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

html_context = {
    "display_github": True,
    "github_user": "mozow01",
    "github_repo": "WebpplHelp",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

# Copy buttons ONLY for source code blocks (WebPPL is highlighted as javascript)
copybutton_selector = "div.highlight-javascript pre, div.highlight-js pre"

# Never copy line numbers, prompts, or console outputs (Pygments classes)
copybutton_exclude = ".linenos, .gp, .go"
