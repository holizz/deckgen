#!/usr/bin/env python

from distutils.core import setup, Command
import unittest

class TestCommand(Command):
    """Run tests"""

    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        loader = unittest.TestLoader()
        t = unittest.TextTestRunner()
        t.run(loader.discover('test'))

setup(
        name = 'deckgen',
        description = 'Mental poker shuffling and card-revealing',
        author = 'Tom Adams',
        author_email = 'tom@holizz.com',
        packages = ['deckgen'],
        requires = [
            'mock',
            'pycrypto',
            ],
        cmdclass = {
                'test': TestCommand,
            },
    )
