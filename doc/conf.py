# -*- coding: utf-8 -*-

import json

import param

param.parameterized.docstring_signature = False
param.parameterized.docstring_describe_params = False

from nbsite.shared_conf import *  # noqa
from nbsite.shared_conf import setup as nbsite_setup

project = 'param'
authors = 'HoloViz developers'
copyright_years['start_year'] = '2003'  # noqa
copyright = copyright_fmt.format(**copyright_years)  # noqa
description = 'Declarative Python programming using Parameters'

version = release = base_version(param.__version__)  # noqa

nbbuild_cell_timeout = 600

html_static_path += ['_static']  # noqa

html_logo = "_static/logo_horizontal.png"

html_favicon = "_static/favicon.ico"

exclude_patterns = ['governance/**/*.*', 'Promo.ipynb']

html_theme_options = {
    "github_url": "https://github.com/holoviz/param",
    "icon_links": [
        {
            'name': 'Twitter',
            'url': 'https://twitter.com/holoviz_org',
            'icon': 'fa-brands fa-twitter-square',
        },
        {
            "name": "Discourse",
            "url": "https://discourse.holoviz.org/",
            "icon": "fa-brands fa-discourse",
        },
        {
            "name": "Discord",
            "url": "https://discord.gg/AXRHnJU6sP",
            "icon": "fa-brands fa-discord",
        },
    ],
    "navbar_start": ["navbar-logo", "version-switcher"],
    "footer_start": [
        "copyright",
        "last-updated",
    ],
    "analytics": {"google_analytics_id": 'G-KD5GGLCB54'},
    "switcher": {
        "json_url": "http://param.holoviz.org.s3-website-us-east-1.amazonaws.com/en/latest/_static/switcher.json",
    }

}

extensions += [  # noqa
    'sphinx_copybutton',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx_remove_toctrees'
]
remove_from_toctrees = ["reference/param/generated/*"]

# Override the Sphinx default title that appends `documentation`
html_title = f'{project} v{version}'
# Format of the last updated section in the footer
html_last_updated_fmt = '%Y-%m-%d'

myst_heading_anchors = 3

napoleon_numpy_docstring = True

def add_version(app):
    with open('./switcher.json', 'r') as f:
        versions = json.load(f)
    found = False
    for v in versions:
        if version == v.get('version'):
            found = True
    if not found:
        versions.insert(1, {
            'name': 'Version {version[1:]}',
            'version': version,
            'url': "http://param.holoviz.org.s3-website-us-east-1.amazonaws.com/en/{version}/"
        })

    with open('./_static/switcher.json', 'w') as f:
        json.dump(versions, f)

def setup(app):
    nbsite_setup(app)
    app.connect('builder-inited', add_version)
