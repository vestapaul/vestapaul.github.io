#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import pelican_youtube

AUTHOR = u'vestapaul'
SITENAME = u'Paul Stauskas'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('The Steel Guitar Forum', 'http://bb.steelguitarforum.com/index.php'),
         ('Rady Guide', 'http://www.radyguide.com')

         )

# Social widget
SOCIAL = (('Instagram', 'http://www.instagram.com/vestapaul'),
          ('Facebook', 'http://www.facebook.com/pstauskas'),
          )

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['blog', 'images']

PAGE_PATHS = ['pages']

PAGE_ORDER_BY = 'page-order'

GOOGLE_ANALYTICS = 'UA-102352675-1'

PLUGIN_PATHS = ["plugins", "/Users/pstauskas/vestapaulGitHubPages/vestapaul.github.io/plugins"]
PLUGINS = ['pelican_youtube']
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
