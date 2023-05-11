# using the dictionary to store the cost of each dish
menu = dict(coke=3.0, hamburger=12.5, pizza=14.0)
# the program will ask the name of customer, the dish, and the quantity
name = input("Enter the name of the Customer: ")
# valid dishes include: hamburger, coke, pizza
dish = input("Enter the dish: ")
quantity = input("Enter the dish quantity: ")

customer_list = []
member_list = []

#error handling for valid dish
while True:
    dish = input("Enter the dish: ")
    if dish in menu:
        break
    else:
        print("Invalid dish entered. Please enter a valid dish.")
# using append to add new customer to rewards_list
# enter y to be added to rewards program or n to not join
if name not in member_list:
    member_answer = input("would you like to be in the members program?: ")
    while member_answer != "y" and member_answer != "n":
        member_answer = input("Please enter correct input (y/n): ")
    if member_answer == "y":
        member_list.append(name)

line_total = float(menu[dish]) * float(quantity)
# adding 10% fee to customer not in members program and 0% if they are
service_fee = 0 if name in member_list else line_total * 0.10
total = line_total + service_fee
# This will display the receipt
print(50 * '*')
print("Receipt of Customer: " + name)
print(50 * '*')
print(f'{dish} {str(menu[dish])} (AUD) x {quantity}')
print("Service fee: " + str(service_fee), "(AUD)")
print("total cost: " + str(total), "(AUD)")