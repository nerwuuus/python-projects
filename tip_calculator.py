print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

bill_with_tip = bill + (bill * tip / 100)
# test
# print(bill_with_tip)
bill_split_per_person = round(bill_with_tip / people, 2)
print(f"Everybody should pay ${bill_split_per_person}.")

