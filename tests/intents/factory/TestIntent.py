#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from application.intents.factory.Intent import Intent


class TestIntent(unittest.TestCase):

    def test_from_name(self):
        self.assertEqual(Intent.from_name("florentclarret:PokemonSimpleQuery"), Intent.SIMPLE_QUERY)

    def test_from_name_with_invalid_name(self):
        self.assertRaises(ValueError, Intent.from_name, "florentclarret:PokemonUnknownIntent")


if __name__ == '__main__':
    unittest.main()
