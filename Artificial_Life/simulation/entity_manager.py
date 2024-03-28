import random
from simulation_constants import (
    HEALTH_RANGE,
    ENERGY_RANGE,
    ENERGY_CONSUMPTION,
    ENERGY_REPLENISHMENT,
)

class Entity:
    def __init__(self, position=(0, 0)):
        self.health = random.randint(*HEALTH_RANGE)
        self.energy = random.randint(*ENERGY_RANGE)
        self.position = position

    def update(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Plant(Entity):
    def update(self):
        # Plants do not have specific behavior for now
        pass

class Herbivore(Entity):
    def update(self):
        self.energy -= ENERGY_CONSUMPTION
        if self.energy <= 0:
            self.health -= 10
        # Simulate eating
        self.energy += ENERGY_REPLENISHMENT
        if self.health <= 0:
            print("Herbivore died of starvation")
        else:
            print("Herbivore foraging")

class Carnivore(Entity):
    def update(self):
        self.energy -= ENERGY_CONSUMPTION
        if self.energy <= 0:
            self.health -= 10
        # Simulate hunting success
        self.energy += ENERGY_REPLENISHMENT // 2
        if self.health <= 0:
            print("Carnivore died of starvation")
        else:
            print("Carnivore hunting")

class Omnivore(Entity):
    def update(self):
        self.energy -= ENERGY_CONSUMPTION
        if self.energy <= 0:
            self.health -= 5
        # Simulate scavenging success
        self.energy += ENERGY_REPLENISHMENT
        if self.health <= 0:
            print("Omnivore died of starvation")
        else:
            print("Omnivore scavenging")

class EntityManager:
    def __init__(self, reporter=None):
        self.entities = []
        self.reporter = reporter

    def add_entity(self, entity):
        self.entities.append(entity)
        print(f"Entity added: {entity}")
        if self.reporter:
            self.reporter.log_entity_birth(type(entity).__name__, entity.position)

    def remove_entity(self, entity):
        try:
            self.entities.remove(entity)
            print(f"Entity removed: {entity}")
            if self.reporter:
                self.reporter.log_entity_death(type(entity).__name__, entity.position)
        except ValueError as e:
            print(f"Error removing entity: {e}")
            if self.reporter:
                self.reporter.log_event(f"Error removing entity: {e}")

    def update_entities(self, reporter=None):
        entities_to_remove = []
        for entity in self.entities[:]:
            try:
                entity.update()
                if entity.health <= 0:
                    entities_to_remove.append(entity)
            except Exception as e:
                print(f"Error updating entity: {e}")
                if reporter:
                    reporter.log_event(f"Error updating entity: {e}")
        for entity in entities_to_remove:
            self.remove_entity(entity)

# Example usage
if __name__ == "__main__":
    manager = EntityManager()
    manager.add_entity(Herbivore())
    manager.add_entity(Carnivore())
    manager.update_entities()