from setuptools import setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

description = "This is small Python package which encode standard " \
              "timestamp to shorted form by using alphabetic symbols."

setup(
    name='alphabetic_timestamp',
    version='1.0',
    packages=['alphabetic_timestamp'],
    url='https://github.com/ShadowCodeCz/alphabetic_timestamp',
    author='ShadowCodeCz',
    author_email='shadow.code.cz@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=classifiers,
    keywords=["timestamp", "alphabetic"]
)
