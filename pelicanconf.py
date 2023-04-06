
#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import time

AUTHOR = 'Andrea Titton'
SITENAME = 'Andrea Titton'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Custom settings for my own site to use in the copyright notice.
CURRENT_YEAR = time.strftime("%Y")

THEME = 'theme'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
    },
    'output_format': 'html5',
    'lazy_ol': False
}

DISPLAY_PAGES_ON_MENU = True

PLUGIN_PATHS = ['./activate_plugins']
PLUGINS = ['render_math']
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extras/custom.css': {'path': 'static/custom.css'}
}

CUSTOM_CSS = 'static/custom.css'