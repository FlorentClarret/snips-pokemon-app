#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from application.config.SnipsTools import SnipsConfigParser
from application.pokeapi.PokeApi import PokeApi


class TestPokeApi(unittest.TestCase):

    def setUp(self):
        self.config = SnipsConfigParser.read_configuration_file("config.ini")

    def test_get_pokemon(self):
        api = PokeApi(self.config)
        pikachu_json = api.get_pokemon("pikachu")
        self.assertIsNotNone(pikachu_json)
        self.assertEqual(pikachu_json.get("id"), 25)
        self.assertEqual(pikachu_json.get("name"), "pikachu")


if __name__ == '__main__':
    unittest.main()
