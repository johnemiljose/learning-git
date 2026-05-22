# Day 1 Tip Calculator

print("Welcome to the tip calculator.")

# gather inputs from the user
bill_input = input("What was the total bill? ₹ ")
tip_input = input("What percentage tip would you like to give? 10, 12 or 15?")
people_input = input("How many people to split the bill? ")

# convert string inputs into numbers (Type casting)
bill = float(bill_input)
tip_percentage = int(tip_input)
people = int(people_input)

# calculate the total per person
# calculate the total bill including the tip percentage
total_bill = bill * (1 + tip_percentage/100)
# Split the total bill by the number of people
amount_per_person = total_bill / people

# Format the result to always 2 decimal places 
final_amount = "{:.2f}".format(amount_per_person)

print(f"Each person should pay: ₹{final_amount}")