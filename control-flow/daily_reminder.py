# daily_reminder.py

def get_input(prompt, valid_options=None):
    while True:
        value = input(prompt).strip().lower()
        if valid_options:
            if value in valid_options:
                return value
            else:
                print(f"Please enter one of the following: {', '.join(valid_options)}")
        else:
            if value:
                return value
            else:
                print("Input cannot be empty.")

def main():
    task = get_input("Enter your task: ", None)
    priority = get_input("Priority (high/medium/low): ", ["high", "medium", "low"])
    time_bound = get_input("Is it time-bound? (yes/no): ", ["yes", "no"])

    match priority:
        case "high":
            msg = f"Reminder: '{task}' is a high priority task"
        case "medium":
            msg = f"Reminder: '{task}' is a medium priority task"
        case "low":
            msg = f"Note: '{task}' is a low priority task"

    if time_bound == "yes":
        if priority in ["high", "medium"]:
            print(f"{msg} that requires immediate attention today!")
        else:
            print(f"{msg} that you might want to finish soon.")
    else:  # time_bound == "no"
        if priority == "low":
            print(f"{msg}. Consider completing it when you have free time.")
        else:
            print(f"{msg}. You can plan to complete it as per your schedule.")

    print("\nWell done on completing this project! Let the world hear about this milestone achieved.\n")
    print("🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    main()

