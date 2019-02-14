#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class Intent(Enum):
    SIMPLE_QUERY = "florentclarret:PokemonSimpleQuery"

    @staticmethod
    def from_name(name):
        for intent in Intent:
            if intent.value == name:
                return intent

        raise ValueError("Intent {} is unknown".format(name))
