#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents.SimplePokemonIntent import SimplePokemonIntent


class PokemonIdIntent(SimplePokemonIntent):

    def __init__(self, config):
        super().__init__(config, "Its id is {}", "id")
