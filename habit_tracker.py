import datetime

def load_habits():
    try:
        with open("habits.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_habits(habits):
    with open("habits.txt", "w") as file:
        for habit in habits:
            file.write(f"{habit}\n")

def add_habit(habits):
    habit = input("Enter the habit you want to track: ")
    habits.append(f"{habit} - Last tracked: {datetime.date.today()}")
    print(f"Added '{habit}' to your habits!")

def view_habits(habits):
    if not habits:
        print("No habits found. Add some habits to track!")
    else:
        print("Your habits:")
        for i, habit in enumerate(habits, 1):
            print(f"{i}. {habit}")

def main():
    habits = load_habits()
    while True:
        print("\nHabit Tracker")
        print("1. View Habits")
        print("2. Add Habit")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            view_habits(habits)
        elif choice == '2':
            add_habit(habits)
        elif choice == '3':
            save_habits(habits)
            print("Your habits have been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
