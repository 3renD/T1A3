# using the dictionary to store the cost of each dish
menu = dict(coke=3.0, burger=12.5, pizza=14.0)
#lists
customer_list = []
member_list = []

#menu list
while True:
    print("Welcome to the restaurant ordering system!")
#     print("Please select an option:")
#     print("1. Order a meal")
#     print("2. Display existing customers information")
#     print("3. Display existing dishes information")
#     print("4. Exit the program")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name of the Customer: ")
    #dish + error handling
        while True:
            dish = input("Enter the dish: ")
            if dish in menu:
                break
            else:
                print("Invalid dish entered. Please enter a valid dish (coke, burger, pizza).")


        # dish quantity + error handling
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
        # enter y to be added to members program or n to not join
        if name not in member_list:
            member_answer = input("would you like to be in the members program? (no service fee will be added): ")
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