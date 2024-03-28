import pygame
from simulation_constants import PLANT, HERBIVORE, CARNIVORE, OMNIVORE

# Define colors for different entities
COLORS = {
    PLANT: (0, 255, 0),       # Green
    HERBIVORE: (255, 200, 200),  # Light red
    CARNIVORE: (255, 0, 0),   # Red
    OMNIVORE: (100, 100, 255), # Light blue
    "TERRAIN": (250, 250, 250) # Light gray for terrain
}

# Size of each cell in the grid
CELL_SIZE = 10

def render_world(screen, world_state, cycle_number):
    """
    Renders the world state onto the given screen.
    
    :param screen: The pygame surface to draw on.
    :param world_state: A 2D numpy array representing the world grid.
    :param cycle_number: The current cycle number to display.
    """
    # Fill the background with white
    screen.fill(COLORS["TERRAIN"])
    
    # Draw the world entities
    for x in range(world_state.shape[0]):
        for y in range(world_state.shape[1]):
            entity_type = world_state[x, y]
            if entity_type in COLORS:
                color = COLORS[entity_type]
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Display the current cycle number
    font = pygame.font.Font(None, 36)
    text = font.render(f"Cycle: {cycle_number}", True, (0, 0, 0))
    screen.blit(text, (5, 5))
    
    # Update the display
    pygame.display.flip()