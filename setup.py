# -*- coding: utf-8 -*-
from distutils.core import setup
import os


def long_description():
    rfname = os.path.join(os.path.dirname(__file__), 'README.md')
    with open(rfname, 'r') as readme:
        readme_text = readme.read()
    return(readme_text)

setup(name='FileTranscriber',
      version='0.2.1',
      description='''A small utility that simulates user typing to aid \
file transcription in limited environments''',
      long_description=long_description(),
      author='Paul Barton',
      author_email='pablo.barton@gmail.com',
      url='https://github.com/SavinaRoja/FileTranscriber',
      install_requires=['docopt', 'PyUserInput'],
      license='http://opensource.org/licenses/MIT',
      scripts=['transcribe'])
