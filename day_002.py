print("Welcome to tip calculator!!!")

bill = float(input("What is the total bill? "))
tip = float(input("How much tip you would like to give? "))
number_of_people = int(input("How many people to split the bill? "))

total = bill * (1 + tip / 100)

total_splited = total / number_of_people

print(f"Each person should pay ${round(total_splited, 3)}")