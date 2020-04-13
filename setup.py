from setuptools import setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: OS Independent'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

description = "This is small Python package which encode standard " \
              "timestamp to shorted form by using alphabetic symbols."

setup(
    name='alphabetic_timestamp',
    version='1.1.5',
    packages=['alphabetic_timestamp'],
    url='https://github.com/ShadowCodeCz/alphabetic_timestamp',
    project_urls={
        'Source': 'https://github.com/ShadowCodeCz/alphabetic_timestamp',
        'Tracker': 'https://github.com/ShadowCodeCz/alphabetic_timestamp/issues',
    },
    author='ShadowCodeCz',
    author_email='shadow.code.cz@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    keywords='timestamp alphabetic',
    license='GNU Affero General Public License v3 or later (AGPLv3+)'
)
