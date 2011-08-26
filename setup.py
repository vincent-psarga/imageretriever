from setuptools import setup

import sys, os

def get_file_contents(filename):
    file_path = os.path.join(filename)
    this_file = open(file_path)
    contents = this_file.read().strip()
    this_file.close()
    return contents

version = get_file_contents('version.txt')
history = get_file_contents('HISTORY.txt')
readme = get_file_contents('README.rst')
long_desc = "%s\n\n%s" % (readme, history)

setup(
    name = 'imageretriever',
    version = version,
    description = 'A Django package to download missing images on your local instance from the production/preview server.',
    long_description = long_desc,
    # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Programming Language :: Python',
                 'Framework :: Django',
                 ],
    url = 'http://zestsoftware.nl',
    author = 'Zest Software',
    author_email = 'info@zestsoftware.nl',
    license = 'GPL',
    packages = ['imageretriever'],
    include_package_data=True,
    zip_safe=False,
    install_requires = ['setuptools'],
)
