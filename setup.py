from setuptools import setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: OS Independent'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

description = "This is small Python package which encode standard " \
              "timestamp to shorted form by using alphabetic symbols."

setup(
    name='alphabetic_timestamp',
    version='1.0',
    packages=['alphabetic_timestamp'],
    url='',
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
    python_requires='>=3.6',
    license='GNU Affero General Public License v3 or later (AGPLv3+)'
)