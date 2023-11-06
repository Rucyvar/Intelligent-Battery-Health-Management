import random
import numpy as np
from sklearn.tree import DecisionTreeRegressor

class BatteryHealthImprovement:
    def _init_(self):
        self.battery_health = 0.9  # Initial battery health score
        self.battery_capacity = 5.0  # Initial battery capacity (in ampere-hours)
        self.battery_life_model = DecisionTreeRegressor()

        self.cycles = 0  # Track the number of cycles

    def collect_data(self, cycles, health_scores):
        self.cycle_data = np.array(cycles).reshape(-1, 1)
        self.health_data = np.array(health_scores)

    def train_life_prediction_model(self):
        self.battery_life_model.fit(self.cycle_data, self.health_data)

    def predict_battery_health(self, cycles):
        predicted_health = self.battery_life_model.predict(np.array(cycles).reshape(-1, 1))
        return predicted_health[0]

    def check_battery_health(self):
        self.battery_health = max(0.0, min(1.0, self.battery_health - random.uniform(0.02, 0.08)))
        self.cycles += 1  # Increase cycle count
        return self.battery_health

class TwoWheelerIgnitionSystem:
    def _init_(self):
        self.battery_health_improvement = BatteryHealthImprovement()
        self.engine_status = False  # Engine status (off by default)

    def start_engine(self):
        if self.engine_status:
            return "Engine is already running."
        else:
            self.engine_status = True
            return "Engine started successfully."

    def stop_engine(self):
        if not self.engine_status:
            return "Engine is already off."
        else:
            self.engine_status = False
            return "Engine stopped successfully."

    def suggest_operational_changes(self):
        suggestions = []
        if self.battery_health_improvement.battery_health < 0.6:
            suggestions.append("Avoid long idling periods. It can drain the battery.")
        if self.battery_health_improvement.battery_health < 0.4:
            suggestions.append("Turn off lights and accessories when the engine is not running.")
        if self.battery_health_improvement.battery_health < 0.3:
            suggestions.append("Consider using a battery tender or maintainer when the vehicle is not in use for an extended period.")
        return suggestions

def main():
    ignition_system = TwoWheelerIgnitionSystem()

    # Generate synthetic data for training the model
    cycles = [100, 200, 300, 400, 500]
    health_scores = [0.9, 0.85, 0.75, 0.7, 0.65]

    ignition_system.battery_health_improvement.collect_data(cycles, health_scores)
    ignition_system.battery_health_improvement.train_life_prediction_model()

    print("2-Wheeler Vehicle Ignition System Model")
    
    while True:
        print("\nOptions:")
        print("1. Start Engine")
        print("2. Stop Engine")
        print("3. Suggest Operational Changes")
        print("4. Predict Battery Health")
        print("5. Show Battery Status")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(ignition_system.start_engine())
        elif choice == '2':
            print(ignition_system.stop_engine())
        elif choice == '3':
            suggestions = ignition_system.suggest_operational_changes()
            if suggestions:
                print("Operational Change Suggestions:")
                for suggestion in suggestions:
                    print(f"- {suggestion}")
            else:
                print("No suggestions at the moment.")
        elif choice == '4':
            cycles_input = int(input("Enter the number of cycles: "))
            predicted_health = ignition_system.battery_health_improvement.predict_battery_health(cycles_input)
            print(f"Predicted Battery Health: {predicted_health:.2f}")
        elif choice == '5':
            battery_health = ignition_system.battery_health_improvement.battery_health
            cycles = ignition_system.battery_health_improvement.cycles
            print(f"Battery Health: {battery_health:.2f}")
            print(f"Cycle Count: {cycles}")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    main()