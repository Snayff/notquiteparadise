
# Not Quite Paradise
Possibly, one day, a roguelike.

## Badges
Current position:

![GitHub tag (latest by date
  )](https://img.shields.io/github/v/tag/Snayff/notquiteparadise?label=version)
 [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Snayff_notquiteparadise&metric=ncloc)](https://sonarcloud.io/dashboard?id=Snayff_notquiteparadise)

Quality of last commit:  

 ![GitHub
 Workflow Status](https://img.shields.io/github/workflow/status/Snayff/notquiteparadise/Not%20Quite%20Paradise) 
 [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
 
 
 Quality of repo:
 
 [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Snayff_notquiteparadise&metric=coverage)](https://sonarcloud.io/dashboard?id=Snayff_notquiteparadise)
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
- [NQP MVP Roadmap](#nqp-mvp-roadmap)
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
* [ ] Interaction-focused - initial tag systems are in place but are yet to be embedded across the different systems
. Basic interactions between actions and entities are in place.   
 

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
See the [Contributing] document for details in how you can get involved.

[Contributing]: CONTRIBUTING.md

## NQP MVP Roadmap
Following advice from a knowledgeable sage, for the time being this project is focused on achieving an MVP. That is
 to say that the aim is to achieve a basic level of functionality and a core set of features on which to build.

All planned features and known issues are held on the [NQP Issue Tracker]. 

[NQP Issue Tracker]: https://nqp.myjetbrains.com/youtrack/issues


## License
[MIT](https://tldrlegal.com/license/mit-license)
