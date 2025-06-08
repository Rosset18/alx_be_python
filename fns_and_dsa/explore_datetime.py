from datetime import datetime, timedelta

current_date = datetime.now()

def display_current_datetime():
    # Format the current date and time using "%Y-%m-%d %H:%M:%S"
    formatted_date_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date_time}")

display_current_datetime()

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    delta_time = timedelta(days=number_of_days)
    # Add days to current date
    future_date = current_date + delta_time
    # Return formatted future date as a string
    return future_date.strftime("%Y-%m-%d")

# Call the function and print the returned value
future_date = calculate_future_date()
print(f"Formatted future date: {future_date}")

