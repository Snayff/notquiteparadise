
# Not Quite Paradise
Possibly, one day, a roguelike.

## Badges
Current position:

![GitHub tag (latest by date
  )](https://img.shields.io/github/v/tag/Snayff/notquiteparadise?label=version)
 [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Snayff_notquiteparadise&metric=ncloc)](https://sonarcloud.io/dashboard?id=Snayff_notquiteparadise)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Quality of last commit:  

 ![GitHub
 Workflow Status](https://img.shields.io/github/workflow/status/Snayff/notquiteparadise/Not%20Quite%20Paradise) 
 [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
 
 
 Quality of repo:
 
[![codecov](https://codecov.io/gh/Snayff/notquiteparadise/branch/develop/graph/badge.svg?token=RDFQIMW3OC)](https://codecov.io/gh/Snayff/notquiteparadise/)
 [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Snayff_notquiteparadise&metric=bugs)](https://sonarcloud.io/dashboard?id=Snayff_notquiteparadise)
 [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=Snayff_notquiteparadise&metric=code_smells)](https://sonarcloud.io/dashboard?id=Snayff_notquiteparadise)
 
 [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Snayff_notquiteparadise&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=Snayff_notquiteparadise)
 [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Snayff_notquiteparadise&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=Snayff_notquiteparadise)
  [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Snayff_notquiteparadise&metric=sqale_index)](https://sonarcloud.io/dashboard?id=Snayff_notquiteparadise)
  



## Table of Contents
- [Motivation and Intent](#motivation-and-intent)
- [Design Goals](#design-goals-&-pillars)
- [Documentation](#documentation)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [NQP Roadmap](#nqp-roadmap)
- [NQP Philosophies](#nqp-philosophies)
- [License](#license)

## Motivation and Intent
To create a fast, dynamic, combat-focused, traditional roguelike where the environment, enemies and even the
 gods all respond to your actions. 
 
 To support this Not Quite Paradise is split into two sections; the engine, aimed at
  being flexible and usable for other projects, and the game, that creates the specific use-cases and rules for the
   gameplay. Eventually these sections will be separated entirely but for now, to simplify development, they are held
    together.

## Design Goals & Pillars
Like a lot of people attempts to make a game ended up creating an engine. As it's grown so to has the ethos behind it
. That ethos is usability first, readability second and performance third. Of course it should be performant, but in
 this case a friendly user experience is more important.   

The design pillars that the NQP engine are as follows:
* [x] Data Driven Design - entities and maps are built using external data held in json files. Skills use external
 data for their values but currently require some internal code to be created. 
* [x] Procedural -  maps are created procedurally.
* [x] Extensible - base classes for all core actions are provided in the engine.
* [x] Composable - built with an entity component system, all entities are expressed by their attached components.
* [x] Explicit - using mypy and consistent naming all methods, functions and classes have a clear purpose.

In progress:
* [ ] Configurable - control remapping is in place ready for controller support, as are the foundations for
 accessibility and player configuration of their game. 
* [ ] Interaction-focused - the interaction system is in place and is easily extensible. As new content is added the interactions  
 

## Documentation
See the project's Github [Pages].

[Pages]: https://snayff.github.io/notquiteparadise/

## Dependencies
The NQP engine has several dependencies, though most of these will be removed over time as the engine is optimised I
 wanted to call out a few special ones that will always be included.
 
 * [snecs] is a blazing fast, super-simple to use [ECS].
 * [python-tcod] is a staple of every python roguelike out there and provides performant field of view, line of sight
  and
  pathfinding operations.
 * [pygame-gui] is an accessible, flexible gui library.
 * [pygame] is an SDL wrapper and provides input handling and rendering.
 
 [snecs]: https://snecs.slavfox.space/
 [ECS]: https://snecs.slavfox.space/ecs/
 [python-tcod]: https://python-tcod.readthedocs.io/en/latest/index.html
 [pygame-gui]: https://pygame-gui.readthedocs.io/en/latest/index.html
 [pygame]: https://www.pygame.org/docs/
 

## Contributing
See the [Contributing] document for details on how you can get involved.

[Contributing]: CONTRIBUTING.md

## NQP Roadmap
Following advice from a knowledgeable sage, for the time being this project is focused on achieving an MVP. That is
 to say that the aim is to achieve a basic level of functionality and a core set of features on which to build.

All planned features and known issues are held on the [NQP Issue Tracker]. 

[NQP Issue Tracker]: https://nqp.myjetbrains.com/youtrack/issues

## NQP Philosophies 
For NQP, the game, the design is underpinned by the following philosophies:
* **Flow** - Periods of impetus to ensure the player is driven forward appropriately. Periods of openness to allow self
 pacing, reflection and exploration.
* **Coherent** - Information pertinent to the player is always made available and easy to parse, utilising a mix of
 art and text. Avoid need for external resource use e.g. a wiki.
* **Flexible**  - Never a best way, always a different one. The only limitations in place should be those that drive
 diversity of play.
* **Accessible** - Supports different kinds of players, e.g. can use keyboard, mouse or controller interchangeably, with
 minimal
 difference in experience. e.g. Colour scheme is colour-blind aware.
* **Customisable** - Near-core game settings can be influenced or set by the player allowing for extensive
 personalisation.

## License
[MIT](https://tldrlegal.com/license/mit-license)
