import csv
from datetime import datetime
import os


class ConditionTracker:
    def __init__(self, filename="condition_tracker.csv"):
        self.filename = filename
        self.headers = [
            "Date",
            "Time",
            # Scalp Metrics
            "Scalp_Flaking",
            "Scalp_Itching",
            "Hair_Fall",
            "New_Growth",
            # Skin Metrics
            "Skin_Redness",
            "Skin_Dryness",
            "Ring_Formation",
            "Ring_Size",
            # Products
            "Morning_Skin_Products",
            "Evening_Skin_Products",
            "Hair_Wash",
            "Shampoo_Used",
            "Oil_Treatment",
            "Oil_Duration",
            # Environmental
            "Temperature",
            "Humidity",
            "Stress_Level",
            "Sleep_Hours",
            "Diet_Changes",
            # Notes
            "Scalp_Notes",
            "Skin_Notes",
            "Triggers",
            # Treatment Phase
            "Week_Number",
            "Current_Phase",
        ]
        self.initialize_file()

    def initialize_file(self):
        """Create the CSV file with headers if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)

    def validate_rating(self, value, field_name):
        """Validate rating inputs (1-5)."""
        try:
            rating = int(value)
            if 1 <= rating <= 5:
                return rating
            else:
                print(f"{field_name} must be between 1 and 5")
                return self.get_valid_rating(field_name)
        except ValueError:
            print(f"Please enter a valid number for {field_name}")
            return self.get_valid_rating(field_name)

    def get_valid_rating(self, field_name):
        """Get valid rating input from user."""
        while True:
            value = input(f"Enter {field_name} (1-5): ")
            try:
                rating = int(value)
                if 1 <= rating <= 5:
                    return rating
            except ValueError:
                print("Please enter a valid number")

    def get_yes_no(self, question):
        """Get valid yes/no input from user."""
        while True:
            response = input(f"{question} (yes/no): ").lower()
            if response in ["yes", "no", "y", "n"]:
                return "Yes" if response in ["yes", "y"] else "No"
            print("Please enter 'yes' or 'no'")

    def add_entry(self):
        """Add a new entry to the tracker."""
        entry = {}
        current_time = datetime.now()

        # Automatically fill date and time
        entry["Date"] = current_time.strftime("%Y-%m-%d")
        entry["Time"] = current_time.strftime("%H:%M")

        # Scalp Metrics
        print("\n=== Scalp Metrics ===")
        entry["Scalp_Flaking"] = self.validate_rating(
            input("Flaking level (1-5): "), "Flaking"
        )
        entry["Scalp_Itching"] = self.validate_rating(
            input("Itching level (1-5): "), "Itching"
        )
        entry["Hair_Fall"] = self.validate_rating(
            input("Hair fall level (1-5): "), "Hair Fall"
        )
        entry["New_Growth"] = self.get_yes_no("Any new growth observed?")

        # Skin Metrics
        print("\n=== Skin Metrics ===")
        entry["Skin_Redness"] = self.validate_rating(
            input("Redness level (1-5): "), "Redness"
        )
        entry["Skin_Dryness"] = self.validate_rating(
            input("Dryness level (1-5): "), "Dryness"
        )
        entry["Ring_Formation"] = self.get_yes_no("Ring formation present?")
        entry["Ring_Size"] = input(
            "Ring size in cm (if applicable, press enter if none): "
        )

        # Products
        print("\n=== Products Used ===")
        entry["Morning_Skin_Products"] = input("Morning skin products used: ")
        entry["Evening_Skin_Products"] = input("Evening skin products used: ")
        entry["Hair_Wash"] = self.get_yes_no("Did you wash your hair today?")
        entry["Shampoo_Used"] = input("Shampoo used (if any): ")
        entry["Oil_Treatment"] = input("Oil treatment used (if any): ")
        entry["Oil_Duration"] = input(
            "Duration of oil treatment (hours, if applicable): "
        )

        # Environmental Factors
        print("\n=== Environmental Factors ===")
        entry["Temperature"] = input("Temperature (°C): ")
        entry["Humidity"] = input("Humidity (%): ")
        entry["Stress_Level"] = self.validate_rating(
            input("Stress level (1-5): "), "Stress"
        )
        entry["Sleep_Hours"] = input("Hours of sleep: ")
        entry["Diet_Changes"] = input("Any notable diet changes: ")

        # Notes
        print("\n=== Notes ===")
        entry["Scalp_Notes"] = input("Scalp observations: ")
        entry["Skin_Notes"] = input("Skin observations: ")
        entry["Triggers"] = input("Any new triggers identified: ")

        # Treatment Phase
        print("\n=== Treatment Phase ===")
        entry["Week_Number"] = input("Week number of treatment: ")
        entry["Current_Phase"] = input(
            "Current phase (Reset/Introduction/Maintenance): "
        )

        # Save to CSV
        with open(self.filename, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writerow(entry)

        print("\nEntry successfully added!")

    def view_last_entry(self):
        """View the most recent entry."""
        try:
            with open(self.filename, "r") as file:
                entries = list(csv.DictReader(file))
                if entries:
                    last_entry = entries[-1]
                    print("\n=== Last Entry ===")
                    for key, value in last_entry.items():
                        print(f"{key}: {value}")
                else:
                    print("No entries found.")
        except FileNotFoundError:
            print("No tracking file found.")


def main():
    tracker = ConditionTracker()
    while True:
        print("\n=== Condition Tracker ===")
        print("1. Add new entry")
        print("2. View last entry")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            tracker.add_entry()
        elif choice == "2":
            tracker.view_last_entry()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
