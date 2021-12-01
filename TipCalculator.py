# As always starting with welcome message

print("Welcome to the tip Calculator.")

#We will takee input from the user i.e the total bill and convert it to float
total_bill = float(input("What was the total bill ? \n$"))

tip = float(input("What percentage tip would you like to give ?\n"))
people = int(input("How many people to split the bill ?\n"))

#After taking all the inputs now its time to do a little math

Total_bill_split = round((total_bill + (total_bill * (tip/100))) / people,2)
print(f"Each person should pay: ${Total_bill_split}")

