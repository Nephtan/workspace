import random
import numpy as np  # Import numpy for handling world_grid as a numpy array
from entity_manager import Plant, Herbivore, Carnivore, Omnivore
from simulation_constants import PLANT, HERBIVORE, CARNIVORE, OMNIVORE

class World:
    def __init__(self, world_grid):
        self.size = world_grid.shape  # Use numpy shape for world dimensions
        self.grid = [[None for _ in range(self.size[1])] for _ in range(self.size[0])]
        self.entities = []

    def add_entity(self, entity):
        if self.grid[entity.position[0]][entity.position[1]] is None:
            self.entities.append(entity)
            self.grid[entity.position[0]][entity.position[1]] = entity
            print(f"Entity {entity} added at {entity.position}")
        else:
            print(f"Position {entity.position} is already occupied.")

    def remove_entity(self, entity):
        self.entities.remove(entity)
        self.grid[entity.position[0]][entity.position[1]] = None
        print(f"Entity {entity} removed from {entity.position}")

    def move_entity(self, entity, new_position):
        if 0 <= new_position[0] < self.size[0] and 0 <= new_position[1] < self.size[1]:
            if self.grid[new_position[0]][new_position[1]] is None:
                self.grid[entity.position[0]][entity.position[1]] = None
                entity.position = new_position
                self.grid[new_position[0]][new_position[1]] = entity
                print(f"Entity {entity} moved to {new_position}")
            else:
                print(f"Position {new_position} is occupied. Movement failed.")
        else:
            print("New position is out of bounds")

    def update_entities(self, reporter=None):
        for entity in self.entities[:]:
            try:
                entity.update()
                if entity.health <= 0:
                    self.remove_entity(entity)
                else:
                    # Simulate random movement
                    new_position = (entity.position[0] + random.randint(-1, 1), entity.position[1] + random.randint(-1, 1))
                    self.move_entity(entity, new_position)
            except Exception as e:
                print(f"Error updating entity: {e}")
                if reporter:
                    reporter.log_event(f"Error updating entity: {e}")
        self.check_collisions()

    def check_collisions(self):
        for entity in self.entities:
            for other_entity in self.entities:
                if entity != other_entity and entity.position == other_entity.position:
                    self.handle_collision(entity, other_entity)

    def handle_collision(self, entity1, entity2):
        print(f"Collision detected between {entity1} and {entity2} at {entity1.position}")
        # Example collision handling logic
        # This could be expanded to include specific interactions like fighting or eating

    def get_entities(self):
        return self.entities

    def log_state(self):
        for row in self.grid:
            print(" ".join([str(entity) if entity else '.' for entity in row]))

    def populate_initial_entities(self, reporter=None):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                entity_type = self.grid[x][y]
                if entity_type == PLANT:
                    self.add_entity(Plant(position=(x, y)))
                elif entity_type == HERBIVORE:
                    self.add_entity(Herbivore(position=(x, y)))
                elif entity_type == CARNIVORE:
                    self.add_entity(Carnivore(position=(x, y)))
                elif entity_type == OMNIVORE:
                    self.add_entity(Omnivore(position=(x, y)))
                if reporter and entity_type in [PLANT, HERBIVORE, CARNIVORE, OMNIVORE]:
                    reporter.log_entity_birth(entity_type, (x, y))