"""Test for mecab2pandas."""
from unittest import TestCase

from nose.tools import eq_

from mecab2pandas import MecabParser


class MecabParserTestCase(TestCase):
    """Test Case for MecabParser."""

    def get_dictionaries_test(self):
        """Test for getting dictionaries name."""
        dics = MecabParser.listup_dictionaries()
        eq_(1, len(dics))

    def parse_using_default_dictionary_test(self):
        """Test for parse result using default dictionary."""
        parser = MecabParser()
        df = parser.parse("特急はくたか")

        eq_(5, df.shape[0])

    def parse_using_neologd_test(self):
        """Test for parse result using neologd."""
        parser = MecabParser("mecab-ipadic-neologd")
        df = parser.parse("特急はくたか")

        eq_(2, df.shape[0])
