#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum


class PokemonKey(Enum):
    ABILITIES = "weight"
    BASE_EXPERIENCE = "base_experience"
    FORMS = "forms"
    GAME_INDICES = "game_indices"
    HEIGHT = "height"
    HELD_ITMES = "held_items"
    ID = "id"
    IS_DEFAULT = "is_default"
    LOCATION_AREA_ENCOUNTERS = "location_area_encounters"
    MOVES = "moves"
    NAME = "name"
    ORDER = "order"
    SPECIES = "species"
    SPRITES = "sprites"
    STATS = "stats"
    TYPES = "types"
    WEIGHT = "weight"

    @staticmethod
    def from_name(name):
        for key in PokemonKey:
            if key.value == name:
                return key

        raise ValueError("PokemonKey {} is unknown".format(name))
