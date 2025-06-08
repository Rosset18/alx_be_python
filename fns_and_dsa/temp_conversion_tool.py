FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Get user input
value_to_be_converted = float(input("Enter the temperature to convert: "))  # Use float for decimal values
choose_temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

# Conversion functions
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Input validation and conversion
if choose_temperature == "c":
    # Convert Celsius to Fahrenheit
    fahrenheit = convert_to_fahrenheit(value_to_be_converted)
    print(f"{value_to_be_converted}°C is {fahrenheit:.2f}°F")
elif choose_temperature == "f":
    # Convert Fahrenheit to Celsius
    celsius = convert_to_celsius(value_to_be_converted)
    print(f"{value_to_be_converted}°F is {celsius:.2f}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")
