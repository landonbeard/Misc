# Import the datetime module to use later
import datetime

# Create an empty list to store the feedings
feedings = []

# Create a function that adds a feeding to the list
def add_feeding(time, amount):
  feedings.append({
    "time": time,
    "amount": amount
  })

# Create a function that prints the total number of feedings for a given date
def print_total_feedings(date):
  # Initialize a counter for the number of feedings
  total_feedings = 0

  # Iterate over the feedings and count the number that occurred on the given date
  for feeding in feedings:
    if feeding["time"].date() == date:
      total_feedings += 1

  # Print the total number of feedings
  print(f"On {date}, the baby was fed {total_feedings} times.")

# Continuously prompt the user for input until they enter "q"
while True:
  print("What would you like to do? (a = add, p = print, q = quit)")
  user_input = input()

  # If the user wants to add a feeding, prompt for the time and amount
  if user_input == "a":
    print("Enter the time of the feeding in the format YYYY-MM-DD HH:MM:SS:")
    time = datetime.datetime.fromisoformat(input())

    print("Enter the amount of food in ounces:")
    amount = float(input())

    add_feeding(time, amount)

  # If the user wants to print the feedings, prompt for the date
  elif user_input == "p":
    print("Enter the date in the format YYYY-MM-DD:")
    date = datetime.datetime.fromisoformat(input()).date()

    print_total_feedings(date)

  # If the user wants to quit, break out of the loop
  elif user_input == "q":
    break
