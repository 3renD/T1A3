

menu = dict(
    burger=12.0,
    wrap=10.5,
    pizza=15.0,
    chips=4.5,
    drink=3.5   
)

# print(menu)

# customers = []
# customers.append(input("what's your name? "))
# print(customers)
# input(f'what would you like {customers[0]}? ')

name = input("Enter the name of the Customer: ")
dish = input("Enter the dish: ")
dish_quantity = input("Enter the dish quantity: ")

total = float(menu[dish]) * float(dish_quantity)

print('************************************************')
print("Receipt of Customer: " + name)
print("************************************************")
print(f'{dish} ${str(menu[dish])} x {dish_quantity}')
print("total cost: $" + str(total))