
# Not Quite Paradise
Possibly, one day, a roguelike.

![GitHub tag (latest by date
  )](https://img.shields.io/github/v/tag/Snayff/notquiteparadise?label=version)
  
  ![GitHub
 Workflow Status](https://img.shields.io/github/workflow/status/Snayff/notquiteparadise/Not%20Quite%20Paradise
 )  ![Code Climate coverage](https://img.shields.io/codeclimate/coverage/Snayff/notquiteparadise) ![Code Climate
  maintainability](https://img.shields.io/codeclimate/maintainability/Snayff/notquiteparadise) ![Code Climate
  technical debt](https://img.shields.io/codeclimate/tech-debt/Snayff/notquiteparadise) 


## Motivation
Create a fast, dynamic, combat-focused, traditional roguelike where the environment, enemies and even the gods all
 respond to your
 actions. 

## Quick Start
This project uses [poetry], an amazing dependency management library.

```shell
python -m pip install --upgrade poetry
poetry install
python -m scripts
```

[poetry]: https://python-poetry.org/

## Contributing
See the [Contributing] document.

[Contributing]: CONTRIBUTING.md

## MVP Roadmap
Following advice from a knowledgeable sage, for the time being this project is focused on achieving an MVP. That is
 to say that each of the following milestones may be in place to some extent but unless ticked they do not meet the
  standard expected for that MVP.
   
Each of the following milestones are subdivided into different, smaller pieces.  They don't necessarily need to be
done in any particular order, but some of them may be dependant on others.

Past MVP, all planned features and known issues are held on the [NQP Issue Tracker]. 

[NQP Issue Tracker]: https://nqp.myjetbrains.com/youtrack/issues

### 0.1 Building a Structure
This update focuses on getting the project setup in a clean manner to allow for fast and productive development. This
 will provide the basic structure and building blocks needed to move forward.

#### Project
* [x] Organize code base
* [ ] Reduce size of large functions & methods 
* [ ] Make code installable
* [ ] Setup github workflows
* [x] Add Quick Start installation instructions
* [x] Add Contribution instructions
* [ ] Setup test infrastructure

#### Engine
* [x] Add renderer
* [x] Add simple data structures for game level objects (e.g. maps, entities)
* [ ] Add algorithm for simple map generation
* [ ] Add basic configuration
* [ ] Build cli

#### Game
* [ ] Add debug/wizard mode
* [x] Add an entity for the main player
* [x] Generate an arena map (single "room")
* [x] Display map
* [x] Add a single enemy

### 0.2 Provide Simple Gameplay
This update aims to add the basic foundations of gameplay, such as movement, combat and simple serialisation.

### Engine
* [ ] Add path finding algorithms
* [ ] Add a way to generate maps from hand annotated files
* [ ] Add a way to store game state
* [ ] Add a way to restore game state
* [ ] Sprinkle debug mode everywhere
* [ ] Make control set configurable on start


### Game
* [x] Add enemy types
* [ ] Add "chase" mechanism for all enemies in a room
* [x] Add simple damage mechanics
* [ ] Add npc spawning capabilities (using wizard mode)
* [x] Add tiles that block movement, e.g. walls
* [ ] Add movement controls for the player
    * [ ] Add VIM controls preset
    * [ ] Add WASD controls preset
    * [x] Add ARROW controls preset

### 0.3 Offer an End
This update will allow the player to win or lose and will provide some basic tools to support balancing combat. This
 will also introduce skills.

#### Engine
* [ ] Add Skills.
* [ ] Add Projectiles, which transport skill effects.
* [ ] Create a tool that can simulate combat to generate combat statistics:
    * [ ] win/loss for a specific npc type
    * [ ] skill effectiveness
    * [ ] benchmarking time to live

#### Game
* [ ] Allow player and npcs to use skills
* [ ] Create 2 different skills 

    
### 0.4 Sharing the Results
This update will allow someone to play the game.

#### Project
* [ ] Create a distributable binary for playing on supported architectures (e.g. linux, windows, mac)
* [ ] Update pipelines to generate distribution based on git tag
