# Obtain shared config values
import sys
from os.path import abspath, join, dirname
from datetime import datetime

import alabaster

sys.path.append(abspath(join(dirname(__file__), '..')))
sys.path.append(abspath(join(dirname(__file__), '..', '..')))

extensions = []

# Enable autodoc
extensions.extend(['sphinx.ext.autodoc', 'sphinx.ext.autosummary'])
autosummary_generate = True

# Enable doctest
extensions.append('sphinxcontrib.autorun')

# Alabaster theme + mini-extension
html_theme_path = [alabaster.get_path()]
extensions.append('alabaster')

# Generating changelog
extensions.append('releases')
releases_issue_uri = "https://github.con/kamilchm/developer-experience/issues/%s"
releases_release_uri = "https://github.con/kamilchm/developer-experience/tree/%s"

# Paths relative to invoking conf.py - not this shared file
html_static_path = ['_static']
html_theme = 'alabaster'
html_theme_options = {
    'logo': 'hn_hat.png',
    'logo_name': True,
    'logo_text_align': 'center',
    'travis_button': False,
    'github_button': True,
    'github_user': 'kamilchm',
    'github_repo': 'developer-experience',
    'link': '#3782BE',
    'link_hover': '#3782BE',
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ]
}

# Regular settings
project = 'HackerNews CLI'
year = datetime.now().year
copyright = '%d Kamil Chmielewski' % year
master_doc = 'index'
templates_path = ['_templates']
exclude_trees = ['_build']
source_suffix = '.rst'
default_role = 'obj'
