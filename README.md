# The Snips Pokémon Application

## Purpose

This application is a [Snips](https://snips.ai/ "Snips's Homepage") assistant made to interact with the [PokeApi](https://pokeapi.co/ "PokeApi's Homepage").

This is my very first Snips application AND python project. I'm using it to learn both so do not expect this project to be perfect. I'm trying to not use any already existing wrapper for this API.

By default, this application hits the online PokeApi services. You can self-host it if you wish and want to be completely offline (Snips is working offline, so the raspberry does not need to be connected to the Internet).

## Available features 

This is a work in progress application. You will find the available features in the following sections :

* Return the id of a specific Pokémon.
* Return the name of a Pokémon using it's id.

### Pokémon's id

#### Intent

| Intent | Slots | Value | 
| --- | --- | --- |
| PokemonId | pokemon | The Pokemon's name |

#### Training examples

| Intent | Example |  
| --- | --- | 
| PokemonId | What is the id of *pokemon*? | 
| PokemonId | Which id is *pokemon*? | 
| PokemonId | What is *pokemon*'s id? | 

Example : 

* Question : *Hey Snips, what is the id of Pikachu?*
* Answer : *The Pikachu's id is 35.*

### Pokémon's name 

#### Intent

| Intent | Slots | Value | 
| --- | --- | --- |
| PokemonName | pokemon | The Pokemon's id |

#### Training examples

| Intent | Example |  
| --- | --- | 
| PokemonName | Give me the name of the *pokemon*? | 
| PokemonName | How is called the *pokemon*? | 
| PokemonName | What is the name of the *pokemon*? | 

Example : 

* Question : *Hey Snips, what is the name of the pokemon number 35?*
* Answer : *Its name is Pikachu.*

## Hardware

I'm testing this application on a Raspberry 3B+ with a ReSpeaker 4-Mic Array.

## Contribute

If you have any idea or if you're willing to contribute, don't hesitate to do it via an issue or a PR.

## License

This project is under the MIT license.