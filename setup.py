# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup
try:
    from ipythonpip import cmdclass
except:
    cmdclass = lambda *args: None

setup(
    name='mywidget',
    version='0.1',
    description='',
    author='',
    author_email='',
    license='',
    url='https://github.com/myname/mywidget',
    keywords='python ipython javascript widget mywidget',
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python',
                 'License :: OSI Approved :: MIT License'],
    packages=['mywidget'],
    include_package_data=True,
    install_requires=["ipython-pip"],
    cmdclass=cmdclass('mywidget'),
)
