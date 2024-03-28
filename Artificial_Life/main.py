# This is the main entry point for the Artificial_Life application.

import sys
import pygame
from simulation.world_generator import generate_world
from simulation.simulation_loop import run_simulation_cycle
from simulation.renderer import render_world

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Artificial Life Simulation")

    world_state = generate_world()

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            world_state = run_simulation_cycle(world_state)
            render_world(screen, world_state)
            pygame.display.flip()

    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    print("Starting the Artificial_Life application...")
    main()