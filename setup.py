"""Setup for generalgui"""

from setuptools import setup, find_packages


setup(
    name = "generalgui",
    version = "0.0.2",
    description = (""
                   "Added binds and tests for them."
                   " Core features for GUI using Tkinter."
                   ""),
    packages = find_packages(),
    install_requires = ["wheel", "generallibrary", "generalvector", "pandas"]
)


