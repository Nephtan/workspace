# Artificial_Life

A simulation application that models an ecosystem with various entities such as plants, herbivores, carnivores, and omnivores interacting in a virtual world. The simulation demonstrates the dynamics of an ecosystem through the life cycle of entities, including their birth, survival actions, and death.

## Overview

The project utilizes Python and Pygame for rendering the simulation's graphical representation. It follows a modular architecture, dividing the responsibilities across different modules:
- `world_generator.py` for initializing the simulation world.
- `entity_manager.py` for managing the entities within the world.
- `simulation_reporter.py` for logging events during the simulation.
- `simulation_loop.py` for running the simulation cycles.
- `renderer.py` for rendering the world state onto a Pygame window.

## Features

- Generation of a random ecosystem with terrain, plants, and animals.
- Entities exhibit behaviors such as foraging, hunting, and scavenging.
- Simulation of entity life cycles including health and energy levels.
- Logging system to report significant simulation events and entity actions.
- Visualization of the simulation world using Pygame.

## Getting started

### Requirements

- Python 3.6 or newer
- Pygame
- Numpy

### Quickstart

1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install pygame numpy
   ```
3. Run the `main.py` script to start the simulation:
   ```bash
   python main.py
   ```

### License

Copyright (c) 2024.