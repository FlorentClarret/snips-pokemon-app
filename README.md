# The Snips Pokémon Application

## Purpose

This application is a [Snips](https://snips.ai/ "Snips's Homepage") assistant made to interact with the [PokeApi](https://pokeapi.co/ "PokeApi's Homepage").

This is my very first Snips application AND python project. I'm using it to learn both so do not expect this project to be perfect. I'm trying to not use any already existing wrapper for this API.

By default, this application hits the online PokeApi services. You can self-host it if you wish and want to be completely offline (Snips is working offline, so the raspberry does not need to be connected to the Internet).

## Available features 

This is a work in progress application. You will find the available features in the following sections :

* Return the id/name/weight/base experience/order/encounters area/height of a specific Pokémon. This is performed in one single intent. I will call it "Pokémon's simple information".

### Pokémon's simple information.

#### Intent

| Intent | Slots | Description | Value | 
| --- | --- | --- | --- |
| PokemonSimpleQuery | PokemonName | The Pokémon's name | Any Pokémon name or there number (eg: Pokémon number 25) |
| PokemonSimpleQuery | PokemonSimpleKey | The "simple" information you want to have | id/name/weight/base experience/order/encounters area/height |

#### Training examples

| Intent | Example |  
| --- | --- | 
| PokemonSimpleQuery | What is the *key* of *Pokémon*? | 
| PokemonSimpleQuery | Give me the *key* of the *Pokémon*. | 
| PokemonSimpleQuery | What is the value of the *key* for *Pokémon*? | 

Example : 

* Question : *Hey Snips, what is the id of Pikachu?*
* Answer : *It's 25.*

Example 2 :

* Question : *Hey Snips, what is the name of the Pokémon number 25?*
* Answer : *It's Pikachu.* 

## Hardware

I'm testing this application on a Raspberry 3B+ with a ReSpeaker 4-Mic Array.

## Contribute

If you have any idea or if you're willing to contribute, don't hesitate to do it via an issue or a PR.

## License

This project is under the MIT license.