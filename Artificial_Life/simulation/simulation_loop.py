import pygame
from world_generator import generate_world
from simulation_reporter import SimulationReporter
from simulation_constants import PLANT, HERBIVORE, CARNIVORE, OMNIVORE
from world import World  # Import the World class to manage the world state
from graphics.renderer import render_world  # Update import path

def run_simulation_cycle(cycles=100, report_interval=10):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Artificial Life Simulation")

    world_grid = generate_world()  # Generate the initial world grid
    world = World(world_grid)  # Create a World instance with the generated grid
    reporter = SimulationReporter()

    world.populate_initial_entities(reporter)  # Use World class method to populate entities

    for cycle in range(1, cycles + 1):
        world.update_entities(reporter)  # Update entities through the World instance
        # Log cycle events or entity actions here if needed

        if cycle % report_interval == 0:
            print(f"Cycle {cycle}/{cycles} completed.")
            # Report current status of the simulation, e.g., number of entities
            reporter.log_world_change(f"Cycle {cycle} completed with {len(world.get_entities())} entities remaining.", cycle=cycle)

        # Render the current state of the world
        render_world(screen, world.grid, cycle)  # Pass cycle number for UI display

        # Handle pygame events to allow for window closing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit the function to stop the simulation

        # Optional: delay between cycles for better visualization
        pygame.time.delay(100)  # Delay in milliseconds

    pygame.quit()

if __name__ == "__main__":
    try:
        reporter = SimulationReporter()  # Initialize the reporter before the try block
        run_simulation_cycle()
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
        reporter.log_event(f"An error occurred during the simulation: {str(e)}")