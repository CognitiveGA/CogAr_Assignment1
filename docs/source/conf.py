# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../cogar_ros2_ws/src'))
print(sys.path)
print("CWD during Sphinx build:", os.getcwd())

show_authors = True
add_module_names = False

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TIAGo Post-earthquake scenario'
copyright = '2025, Group A: Shady Abdelmalek, Francesca Amato, Gian Marco Balia'
author = 'Group A: Shady Abdelmalek, Francesca Amato, Gian Marco Balia'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode',
    'sphinx.ext.todo']

autodoc_mock_imports = [
    "rclpy",
    "std_msgs",
    "sensor_msgs",
    "geometry_msgs",
    "nav_msgs",
    "math",
    "builtin_interfaces",
    "rescue_actuator",
    "rescue_communicator",
    "time",
    "random",
    "json",
    "rescue_core_system",
    "rescue_perception",
    "rescue_search_tasks",
    "rescue_structural_analysis"
]

templates_path = ['_templates']
exclude_patterns = ['*/setup.py']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_show_sourcelink = False

# Initial static context for GitHub repo and user
html_context = {
    "display_github": True,
    "github_user": "CognitiveGA",
    "github_repo": "CogAr_Assignment1",
    "github_version": "main",
    "conf_py_path": "/docs/source/"
}