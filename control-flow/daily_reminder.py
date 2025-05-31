# daily_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            msg = f"Reminder: '{task}' is a high priority task"
        case "medium":
            msg = f"Reminder: '{task}' is a medium priority task"
        case "low":
            msg = f"Note: '{task}' is a low priority task"
        case _:
            print("Invalid priority entered. Please enter high, medium, or low.")
            return

    if time_bound == "yes":
        if priority in ("high", "medium"):
            print(f"{msg} that requires immediate attention today!")
        else:  # low priority but time-bound
            print(f"{msg} that you might want to finish soon.")
    elif time_bound == "no":
        if priority == "low":
            print(f"{msg}. Consider completing it when you have free time.")
        else:
            print(f"{msg}. You can plan to complete it as per your schedule.")
    else:
        print("Invalid input for time-bound. Please enter yes or no.")

if __name__ == "__main__":
    main()

