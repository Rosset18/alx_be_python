# daily_reminder.py

def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            base_msg = f"Reminder: '{task}' is a high priority task"
        case "medium":
            base_msg = f"Reminder: '{task}' is a medium priority task"
        case "low":
            base_msg = f"Note: '{task}' is a low priority task"
        case _:
            print("Invalid priority entered. Please enter high, medium, or low.")
            return

    if time_bound == "yes":
        if priority in ["high", "medium"]:
            print(f"{base_msg} that requires immediate attention today!")
        else:  # low priority but time bound
            print(f"{base_msg} that you might want to finish soon.")
    elif time_bound == "no":
        if priority == "low":
            print(f"{base_msg}. Consider completing it when you have free time.")
        else:
            print(f"{base_msg}. You can plan to complete it as per your schedule.")
    else:
        print("Invalid input for time-bound. Please enter yes or no.")

if __name__ == "__main__":
    main()
