#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from application.intents.factory.Intent import Intent
from application.intents.factory.IntentFactory import IntentFactory
from application.intents.impl.PokemonIdIntent import PokemonIdIntent


class TestIntentFactory(unittest.TestCase):

    def test_build(self):
        self.assertIsInstance(IntentFactory.build(Intent.POKEMON_ID, None), PokemonIdIntent)

    def test_build_with_none(self):
        self.assertRaises(ValueError, IntentFactory.build, None, None)


if __name__ == '__main__':
    unittest.main()
