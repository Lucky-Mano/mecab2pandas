"""Setup script."""
from setuptools import setup

setup(
    name="mecab2pandas",
    version="0.2.1",
    author="Lucky-Mano",
    author_email="phatbowie@gmail.com",
    url="https://github.com/Lucky-Mano/mecab2pandas",
    license="MIT",
    packages=["mecab2pandas"],
    install_requires=["mecab-python3", "pandas"],
)
