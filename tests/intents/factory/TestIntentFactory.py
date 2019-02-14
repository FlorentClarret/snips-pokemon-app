#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from application.intents.factory.Intent import Intent
from application.intents.factory.IntentFactory import IntentFactory
from application.intents.impl.SimplePokemonIntent import SimplePokemonIntent


class TestIntentFactory(unittest.TestCase):

    def test_build(self):
        self.assertIsInstance(IntentFactory.build(Intent.SIMPLE_QUERY, None), SimplePokemonIntent)

    def test_build_with_none(self):
        self.assertRaises(ValueError, IntentFactory.build, None, None)


if __name__ == '__main__':
    unittest.main()
