import pygame
import sys
from entity_manager import EntityManager, Plant, Herbivore, Carnivore, Omnivore

# Initialize pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Initialize EntityManager
entity_manager = EntityManager()

def render_world(entities):
    # Fill the background with white
    screen.fill((255, 255, 255))
    
    # Render entities
    for entity in entities:
        if isinstance(entity, Plant):
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(entity.position[0], entity.position[1], 10, 10))
        elif isinstance(entity, Herbivore):
            pygame.draw.circle(screen, (255, 200, 200), entity.position, 10)
        elif isinstance(entity, Carnivore):
            pygame.draw.circle(screen, (200, 0, 0), entity.position, 10)
        elif isinstance(entity, Omnivore):
            pygame.draw.circle(screen, (100, 100, 255), entity.position, 10)
    
    # Flip the display
    pygame.display.flip()

def main_loop():
    # Main loop flag
    running = True

    # Main loop
    while running:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get current state of entities
        entities = entity_manager.get_entities()
        
        # Render the current state of the world
        render_world(entities)

    # Done! Time to quit.
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()