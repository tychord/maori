
###Task 1
# Function to calculate momentum
def calculate_momentum(mass, velocity):
    momentum = mass * velocity
    return momentum

# Input values for mass (kg) and velocity (m/s)
mass = float(input("Put the mass of the item in kilograms: "))
velocity = float(input("Put the velocity of the item in meters per second: "))

# Calculating momentum
momentum = calculate_momentum(mass, velocity)

# Output the result
print(f"The momentum of the object is {momentum} kg·m/s")

###Task 2
# Calculate Parking Charges
import math
from datetime import datetime

# Function to calculate parking charges
def calculate_parking_fee(hours):
    # Set rates
    rate_first_hour = 4.00        # Cost for the first hour
    rate_additional_hour = 2.50   # Cost for each additional hour
    max_fee_per_day = 20.00       # Maximum fee for a day

    # If parking time is 1 hour or less
    if hours <= 1:
        fee = rate_first_hour
    else:
        # For more than 1 hour, calculate the fee for extra hours
        fee = rate_first_hour + (math.ceil(hours - 1) * rate_additional_hour)

    # Make sure the fee does not exceed the maximum daily rate
    fee = min(fee, max_fee_per_day)

    return fee

# Get input from user for entry and exit time in yy-mm-dd hh:mm:ss format
entry_time_str = input("Enter the entry time (yyyy-mm-dd hh:mm:ss format): ")
exit_time_str = input("Enter the exit time (yyyy-mm-dd hh:mm:ss format): ")

# Convert the input strings to datetime format
entry_time = datetime.strptime(entry_time_str, '%Y-%m-%d %H:%M:%S')
exit_time = datetime.strptime(exit_time_str, '%Y-%m-%d %H:%M:%S')

# Calculate the time difference between entry and exit
time_difference = exit_time - entry_time
# Convert time difference to hours (total seconds divided by 3600)
hours_parked = time_difference.total_seconds() / 3600

# Calculate the parking fee
fee = calculate_parking_fee(hours_parked)

# Display the parking duration and fee
print(f"Parking duration: {hours_parked:.2f} hours")
print(f"Parking fee: ${fee:.2f}")


# Task 3: # Function to calculate electricity charges
def calculate_cost(units, plan_type):
    # Rates and constants
    energy_levy = 0.0013  # Levy per kWh
    low_plan_daily_fee = 0.60  # Daily charge for low user
    standard_plan_daily_fee = 1.891  # Daily charge for standard user
    low_plan_rate = 0.238  # Charge per kWh for low user
    standard_plan_rate = 0.18  # Charge per kWh for standard user
    days_in_month = 30  # Assumed 30 days in a month

    # Calculate charges based on plan type
    if plan_type == "low":
        daily_charge = low_plan_daily_fee * days_in_month  # Total daily charge for low plan
        usage_charge = units * low_plan_rate  # Usage charge based on consumption
    else:
        daily_charge = standard_plan_daily_fee * days_in_month  # Total daily charge for standard plan
        usage_charge = units * standard_plan_rate  # Usage charge for standard plan

    levy_charge = units * energy_levy  # Levy charge on total units consumed
    total_cost = daily_charge + usage_charge + levy_charge  # Total cost

    return total_cost

# List of customers and their consumption levels
customer_data = [
    ("Customer 1", 300),   # 300 kWh consumption
    ("Customer 2", 800),   # 800 kWh consumption
    ("Customer 3", 1600)   # 1600 kWh consumption
]

# Loop through each customer and calculate costs for both plans
for customer_name, consumption in customer_data:
    low_plan_cost = calculate_cost(consumption, "low")  # Calculate for low user plan
    standard_plan_cost = calculate_cost(consumption, "standard")  # Calculate for standard user plan

    # Display the costs and recommendation
    print(f"\n{customer_name} (Consumption: {consumption} kWh):")
    print(f"Low User Plan Cost: ${low_plan_cost:.2f}")
    print(f"Standard User Plan Cost: ${standard_plan_cost:.2f}")

    # Recommend the cheaper plan
    if low_plan_cost < standard_plan_cost:
        print("Recommendation: Low User Plan")
    else:
        print("Recommendation: Standard User Plan")



###Task 4
## Calculating Total weekly Pay
def calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours):
    # Overtime rate is 1.5 times the hourly wage
    overtime_rate = 1.5 * hourly_wage
    
    # Calculating regular pay by multiplying hourly wage and regular hour 
    regular_pay = hourly_wage * regular_hours 
    
    # Calculating  overtime pay  by multiplying overtime rate and over time hours 
    overtime_pay = overtime_rate * overtime_hours
    
    # Calcualting toatal weekly pay which is sum of regular pay and overtime pay
    total_weekly_pay = regular_pay + overtime_pay
    
    return total_weekly_pay

# Main program to get user input and calculate pay
def main():
    # Input: getting data from the user
    hourly_wage = float(input("Enter your hourly wage: "))
    regular_hours = float(input("Enter the total regular hours worked: "))
    overtime_hours = float(input("Enter the total overtime hours worked: "))
    
    # Check if regular hours and overtime hours are valid using logical operators
    if regular_hours >= 0 and overtime_hours >= 0:  # Logical AND operator
        total_pay = calculate_weekly_pay(hourly_wage, regular_hours, overtime_hours)
        print(f"Your total weekly pay is: ${total_pay:.2f}")
    else:
        print("Error: Hours worked must be non-negative.")  # Logical condition to ensure input is valid

# Call the main function to run the program
main()

###Task 5
### Convert Tempeture
# Function to convert temperature
def convert_temperature(te, su, tu):
    # Step 1: Convert the source temperature to Celsius
    if su == "Celsius":
        temp_in_celsius = te
    elif su == "Fahrenheit":
        temp_in_celsius = (te - 32) * 5 / 9  # Convert Fahrenheit to Celsius
    elif su == "kelvin":
        temp_in_celsius = te - 273.15  # Convert Kelvin to Celsius
    else:
        return "Invalid source unit"

    # Step 2: Convert from Celsius to the target unit
    if tu == "Celsius":
        result_temp = temp_in_celsius
    elif tu == "Fahrenheit":
        result_temp = (temp_in_celsius * 9 / 5) + 32  # Convert Celsius to Fahrenheit
    elif tu == "kelvin":
        result_temp = temp_in_celsius + 273.15  # Convert Celsius to Kelvin
    else:
        return "Invalid target unit"

    return result_temp

# Main program to get user input and convert the temperature
def main():
    # Get inputs from the user
    te = float(input("Enter the temperature value: "))
    su = input("Enter the source unit (Celsius, Fahrenheit, kelvin): ")
    tu = input("Enter the target unit (Celsius, Fahrenheit, kelvin): ")

    # Convert the temperature and display the result
    converted_temp = convert_temperature(te, su, tu)

    # Display the result or handle any errors
    if isinstance(converted_temp, str):
        print(converted_temp)  # If there's an error with units
    else:
        print(f"{te} {su} is equal to {converted_temp:.2f} {tu}")

# Run the program
main()


###Task 6
# Function to generate the Fibonacci sequence based on the honeybee breeding pattern
# Function name includes last three digits of Student ID, let's assume 123 as placeholder
def hbfSeqFunc145(N):
    # Initialize an array to store the Fibonacci sequence
    fibonacci_sequence = [1, 1]  # Starting with the first two Fibonacci numbers
    # Generating the Fibonacci sequence up to N numbers
    for i in range(2, N):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)
        
    # Print the first N numbers of the Fibonacci sequence
    print(f"First {N} numbers in the Fibonacci sequence: {fibonacci_sequence}")

    # Print the Nth number in the sequence (Remember, Nth number is at index N-1)
    print(f"The {N}th number in the Fibonacci sequence is: {fibonacci_sequence[N-1]}")
    return
N=int(input("Enter the number for Fibonacci: "))

# Testing the function with N 
hbfSeqFunc145(N)

##Task
# List to store census data
census_list = []

# Function to add a person to the census
def add_person():
    full_name = input("Enter full name: ")
    person_age = int(input("Enter age: "))
    census_list.append([full_name, person_age])  # Add person's details to the list
    print(f"{full_name} has been added to the census data.")

# Function to remove a person from the census
def remove_person():
    full_name = input("Enter the name of the person to remove: ")
    for person in census_list:
        if person[0] == full_name:
            census_list.remove(person)  # Remove person from the list
            print(f"{full_name} has been removed from the census data.")
            return
    print(f"{full_name} not found in the census data.")

# Function to find a person in the census
def find_person():
    full_name = input("Enter the name to search for: ")
    person_age = int(input("Enter the age to search for: "))
    for person in census_list:
        if person[0] == full_name and person[1] == person_age:
            print(f"{full_name}, age {person_age} found in the census data.")
            return
    print(f"No person with name {full_name} and age {person_age} found in the data.")

# Function to sort by name
def sort_by_name(person):
    return person[0]

# Function to sort by age
def sort_by_age(person):
    return person[1]

# Function to sort the census data
def sort_data():
    print("\n1. Sort by name (ascending)")
    print("2. Sort by name (descending)")
    print("3. Sort by age (ascending)")
    print("4. Sort by age (descending)")
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        census_list.sort(key=sort_by_name)  # Sort by name in ascending order
    elif choice == 2:
        census_list.sort(key=sort_by_name, reverse=True)  # Sort by name in descending order
    elif choice == 3:
        census_list.sort(key=sort_by_age)  # Sort by age in ascending order
    elif choice == 4:
        census_list.sort(key=sort_by_age, reverse=True)  # Sort by age in descending order
    else:
        print("Invalid choice.")
        return
    
    print("Census data sorted successfully.")
    if census_list:  # Check if there is data to display
        display_data()  # Show sorted data
    else:
        print("Census data is empty.")  # If no data exists

# Function to display the census data
def display_data():
    if not census_list:
        print("Census data is empty.")
    else:
        print("\nCurrent census data:")
        for person in census_list:
            print(f"Name: {person[0]}, Age: {person[1]}")

# Main program loop
while True:
    print("\n--- Census Data Management ---")
    print("1. Add a person")
    print("2. Remove a person")
    print("3. Find a person")
    print("4. Sort data")
    print("5. Display all data")
    print("6. Exit")
    
    choice = int(input("Enter your choice (1-6): "))
    
    if choice == 1:
        add_person()  # Call function to add a person
    elif choice == 2:
        remove_person()  # Call function to remove a person
    elif choice == 3:
        find_person()  # Call function to find a person
    elif choice == 4:
        sort_data()  # Call function to sort data
    elif choice == 5:
        display_data()  # Call function to display data
    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid choice. Please try again.")


###Task 8
# Initial inventory dictionary
game_inventory = {"bow": 2, "arrow": 20, "gun": 3, "bullet": 100, "rope": 1, "torch": 4, "jacket": 2}

def show_all_items():
    """Displays all items and their quantities in the inventory."""
    print("All items in the inventory:")
    for item_name, item_quantity in game_inventory.items():
        print(f"{item_name}: {item_quantity}")

def show_bullet_quantity():
    """Displays the quantity of bullets in the inventory."""
    bullet_quantity = game_inventory.get("bullet", 0)
    print(f"Number of bullets: {bullet_quantity}")

def show_item_names():
    """Displays all item names from the inventory."""
    print("All item names in the inventory:")
    for item_name in game_inventory.keys():
        print(item_name)

def show_item_quantities():
    """Displays all quantities of items in the inventory."""
    print("All item quantities in the inventory:")
    for item_quantity in game_inventory.values():
        print(item_quantity)

# Main program loop
while True:
    print("\n--- Game Inventory Management ---")
    print("1. Show all items and quantities")
    print("2. Show bullet quantity")
    print("3. Show all item names")
    print("4. Show all item quantities")
    print("5. Exit")
    
    user_choice = input("Enter your choice (1-5): ")
    
    if user_choice == '1':
        show_all_items()
    elif user_choice == '2':
        show_bullet_quantity()
    elif user_choice == '3':
        show_item_names()
    elif user_choice == '4':
        show_item_quantities()
    elif user_choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


