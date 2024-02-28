import os
import sys
sys.path.insert(0, os.path.abspath('./../..'))
sys.path.insert(0, os.path.abspath('./../../libs'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Find_Circularity'
copyright = '2024, Mu-En'
author = 'Mu-En, Dom'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx_rtd_dark_mode',
    'sphinx_mdinclude']

html_theme = 'sphinx_rtd_theme'
default_dark_mode = True
html_css_files = ['custom.css']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

master_doc = 'index'
source_suffix = '.rst'
html_static_path = ['_static']
