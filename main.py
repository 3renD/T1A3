import sys, random, time, math

# using the dictionary to store the name and cost of each dish
menu = dict(coke=3.0, burger=12.5, pizza=14.0)

#lists
customer_list = []
member_list = []

#code block for option 4
def add_dishes_prices():
    #you can add/update dishes by typing (dish name): (price). Add/update multiple dishes by seperating them with a comma.
    dishes_prices = input("Enter new dishes and prices separated by commas (e.g chips: 4, wrap: 6): ")
    try:
        menu.update(dict([dish_price.split(": ") for dish_price in dishes_prices.split(", ")]))
    except ValueError:
        print("Invalid input. Please enter the dish name followed by a colon and then the price.")

#code block for option 2
def display_customers_info():
    if len(customer_list) == 0:
        print("No customers yet.")
    else:
        for customer in customer_list:
            name, dish, quantity, service_fee, total = customer
            member_status = "Member" if name in member_list else "Not Member"
            print(f"Name: {name}, Dish: {dish}, Quantity: {quantity}, Service Fee: {service_fee} (AUD), Total Cost: {total} (AUD), Member Status: {member_status}")

#menu list. Choose the options below by typing the corresponidng number
while True:
    print("Welcome to the restaurant ordering system!")
    print("Please select an option:")
    print("1. Order a meal")
    print("2. Display existing customers information")
    print("3. Display existing dishes information")
    print("4. Add/update dishes and prices")
    print("5. Exit the program")

    choice = input("Enter your choice: ")

#code block for option 1
    if choice == "1":
        name = input("Enter the name of the Customer: ")
        #type in valid dish + error handling
        while True:
            dish = input("Enter the dish: ")
            if dish in menu:
                break
            else:
                print("Invalid dish entered. Please enter a valid dish (coke, burger, pizza).")

        # type in dish quantity + error handling
        while True:
            try:
                quantity = int(input("Enter the dish quantity: "))
                if quantity <= 0:
                    print("Invalid quantity entered. Please enter a valid positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid quantity entered. Please enter a valid positive integer.")

        # members in member program will not have a service fee (10% extra $ to customer order)
        # using append to add new customer to member_list
        # enter y to be added to members program or n to not join + error handling
        if name not in member_list:
            member_answer = input("would you like to be in the members program? (y/n): ")
            while member_answer != "y" and member_answer != "n":
                member_answer = input("Please enter correct input (y/n): ")
            if member_answer == "y":
                member_list.append(name)
        #cost of food
        line_total = float(menu[dish]) * float(quantity)
        # adding 10% fee to customer not in members program and 0% if they are
        service_fee = 0 if name in member_list else line_total * 0.10
        total = line_total + service_fee

        # This will display the receipt
        print(80 * '-')
        print("Receipt of Customer: " + name)
        print(80 * '-')
        print(f'{dish} {str(menu[dish])} (AUD) x {quantity}')
        print("Service fee: " + str(service_fee), "(AUD)")
        print("Total cost: " + str(total), "(AUD)")
        print(80 * '-')

        # adding new customer to customer list
        customer_list.append((name, dish, quantity, service_fee, total))

#option 2 callback
    elif choice == "2":
        display_customers_info()

#option 3 code block
    elif choice == "3":
        for dish in menu:
            price = menu[dish]
            print(f"{dish}: {price} (AUD)")

#option 4 callback
    elif choice == "4":
        add_dishes_prices()

#option 5 code block. Exit program
    elif choice == "5":
        break
#menu option error handle
    else:
        print("Invalid choice entered. Please enter a valid choice.")

print("Thank you for using our program!")