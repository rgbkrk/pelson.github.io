#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Phil Elson'
SITENAME = u"The miscellany of a scientific coder"
SITEURL = '' #'pelson.github.io'
GITHUB_URL = 'http://github.com/pelson/pelson.github.io'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  []

# Social widget
SOCIAL = []

DEFAULT_PAGINATION = False

DISQUS_SITENAME = "pelson"
GOOGLE_ANALYTICS = "UA-43268601-1"


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATH = 'pelican_extras/pelican-plugins'
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook', 'summary']

THEME = "pelican_extras/pelson-custom"