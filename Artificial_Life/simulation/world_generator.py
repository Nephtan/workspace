import numpy as np
import random
from simulation_constants import (
    WORLD_SIZE,
    TERRAIN,
    PLANT,
    HERBIVORE,
    CARNIVORE,
    OMNIVORE,
)

def generate_world():
    """
    Generates the initial state of the game world.
    Returns a 2D numpy array representing the world grid, 
    with randomized terrain and initial placements of plants and critters.
    """
    # Initialize the world grid with terrain
    world = np.full(WORLD_SIZE, TERRAIN, dtype=int)
    
    # Randomly place plants
    for _ in range(random.randint(50, 100)):  # Random number of plants
        x, y = random.randint(0, WORLD_SIZE[0] - 1), random.randint(0, WORLD_SIZE[1] - 1)
        world[x, y] = PLANT
    
    # Randomly place critters (herbivores, carnivores, omnivores)
    for _ in range(random.randint(10, 20)):  # Random number of herbivores
        x, y = random.randint(0, WORLD_SIZE[0] - 1), random.randint(0, WORLD_SIZE[1] - 1)
        world[x, y] = HERBIVORE
    
    for _ in range(random.randint(5, 10)):  # Random number of carnivores
        x, y = random.randint(0, WORLD_SIZE[0] - 1), random.randint(0, WORLD_SIZE[1] - 1)
        world[x, y] = CARNIVORE
    
    for _ in range(random.randint(5, 10)):  # Random number of omnivores
        x, y = random.randint(0, WORLD_SIZE[0] - 1), random.randint(0, WORLD_SIZE[1] - 1)
        world[x, y] = OMNIVORE
    
    return world

if __name__ == "__main__":
    # For testing purposes, generate a world and print its shape
    generated_world = generate_world()
    print("Generated world shape:", generated_world.shape)