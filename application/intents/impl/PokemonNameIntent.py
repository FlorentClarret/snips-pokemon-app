#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from application.intents.SimplePokemonIntent import SimplePokemonIntent


class PokemonNameIntent(SimplePokemonIntent):

    def __init__(self, config):
        super().__init__(config, "Its name is {}", "name")
