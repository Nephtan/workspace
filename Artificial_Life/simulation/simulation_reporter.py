from datetime import datetime

class SimulationReporter:
    def __init__(self, log_file_path="simulation_log.txt"):
        self.log_file = log_file_path

    def log_event(self, event_message, cycle=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cycle_info = f" Cycle {cycle}:" if cycle is not None else ""
        log_message = f"[{timestamp}]{cycle_info} {event_message}"
        try:
            with open(self.log_file, "a") as log:
                log.write(log_message + "\n")
            print(f"Logged event: {log_message}")
        except Exception as e:
            print(f"Error logging event: {e}")

    def log_entity_birth(self, entity_type, position, cycle=None):
        self.log_event(f"New {entity_type} born at {position}", cycle)

    def log_entity_death(self, entity_type, position, cycle=None):
        self.log_event(f"{entity_type} died at {position}", cycle)

    def log_entity_action(self, entity_type, action, position, cycle=None):
        self.log_event(f"{entity_type} at {position} performed action: {action}", cycle)

    def log_world_change(self, change_description, cycle=None):
        self.log_event(f"World changed: {change_description}", cycle)

    def log_summary(self, summary, cycle=None):
        self.log_event(f"Summary: {summary}", cycle)

    def log_cycle_completion(self, cycle, entity_count):
        self.log_event(f"Cycle {cycle} completed with {entity_count} entities remaining.", cycle)

# Example usage
if __name__ == "__main__":
    reporter = SimulationReporter("simulation_log.txt")
    reporter.log_entity_birth("Herbivore", (5, 10), cycle=1)
    reporter.log_entity_action("Carnivore", "hunted", (7, 3), cycle=1)
    reporter.log_world_change("Plant growth in region (2, 2) to (10, 10)", cycle=1)
    reporter.log_summary("End of cycle 1: 5 Herbivores, 3 Carnivores, 20 Plants", cycle=1)
    reporter.log_cycle_completion(1, 28)