# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Structured and Unstructured grid Relocatable ocean platform for Forecasting (SURF)'
copyright = '2020, Francesco'
author = 'Francesco Trotta, Nadia Pinardi'

# The full version, including alpha/beta/rc tags
release = 'V1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = []

extensions.append('sphinx.ext.todo')
extensions.append('sphinx.ext.autodoc')
#extensions.append('sphinx.ext.autosummary')
extensions.append('sphinx.ext.intersphinx')
extensions.append('sphinx.ext.mathjax')
extensions.append('sphinx.ext.viewcode')
extensions.append('sphinx.ext.graphviz')

autosummary_generate = True

# Create numbers on figures with captions
numfig = True

# numfig:
# numfig_number_figures = True
# numfig_figure_caption_prefix = "Figure"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

#---sphinx-themes-----
# html_theme = 'alabaster'



#---sphinx-themes-----
html_theme = "classic"
# html_theme_options = {
#     "relbarbgcolor": "black"
# }

html_theme_options = {
    'collapsiblesidebar': True,
    'externalrefs':True,
    # 'sidebar_span': 6, # 1(min) - 12(max)
    'inner_theme': True,
    'inner_theme_name': 'bootswatch-amelia'
}

# classic – This is the classic theme, which looks like the Python 2 documentation. It can be customized via these options:
#
# rightsidebar (true or false): Put the sidebar on the right side. Defaults to False.
# stickysidebar (true or false): Make the sidebar “fixed” so that it doesn’t scroll out of view for long body content. This may not work well with all browsers. Defaults to False.
# collapsiblesidebar (true or false): Add an experimental JavaScript snippet that makes the sidebar collapsible via a button on its side. Defaults to False.
# externalrefs (true or false): Display external links differently from internal links. Defaults to False.
# There are also various color and font options that can change the color scheme without having to write a custom stylesheet:
#
# footerbgcolor (CSS color): Background color for the footer line.
# footertextcolor (CSS color): Text color for the footer line.
# sidebarbgcolor (CSS color): Background color for the sidebar.
# sidebarbtncolor (CSS color): Background color for the sidebar collapse button (used when collapsiblesidebar is True).
# sidebartextcolor (CSS color): Text color for the sidebar.
# sidebarlinkcolor (CSS color): Link color for the sidebar.
# relbarbgcolor (CSS color): Background color for the relation bar.
# relbartextcolor (CSS color): Text color for the relation bar.
# relbarlinkcolor (CSS color): Link color for the relation bar.
# bgcolor (CSS color): Body background color.
# textcolor (CSS color): Body text color.
# linkcolor (CSS color): Body link color.
# visitedlinkcolor (CSS color): Body color for visited links.
# headbgcolor (CSS color): Background color for headings.
# headtextcolor (CSS color): Text color for headings.
# headlinkcolor (CSS color): Link color for headings.
# codebgcolor (CSS color): Background color for code blocks.
# codetextcolor (CSS color): Default text color for code blocks, if not set differently by the highlighting style.
# bodyfont (CSS font-family): Font for normal text.
# headfont (CSS font-family): Font for headings.


# #---sphinx-themes-----
# html_theme = 'python_docs_theme'
#
# # Theme options are theme-specific and customize the look and feel of a theme
# # further.  For a list of options available for each theme, see the
# # documentation.
# #
# html_theme_options = {
#     'collapsiblesidebar': True,
#     'root_name':'Surf',
#     'root_url':'http://surf.local/',
#     'root_icon':'surflogo2.png',
#     'root_include_title':'True'
# }




# Custom sidebar templates, filenames relative to this file.
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }




# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = []


extensions.append('sphinxcontrib.versioning.sphinx_')
