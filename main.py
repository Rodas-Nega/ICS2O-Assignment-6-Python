#!/usr/bin/ env python3

# Created By Rodas Nega
# Created On January 11 2020
# A program that will calculate the subtotal, tax, and total cost of a pizza with a given size and amount of toppings 


print('Welcome to my pizzaria! What would you like?')
print("")
print('Our pizza sizes are large and extra large.')
print('You can have 1-4 toppings on your pizza.')
print("")
print('Large is $6.00 and Extra large is $10.00')
print('1 topping is $1.00, 2 is $1.75, 3 is $2.50, and 4 is $3.35')
print("")
size = str(input('Type in the size of your pizza:'))
toppings = float(input('Type in the price for the amount of toppings you want:'))
print("")

large = 6
extra = 10
topping_1 = 1
topping_2 = 1.75
topping_3 = 2.5
topping_4 = 3.35
tax = 1.13


if (size == 'Large' or size == 'large') and (toppings == 1 or toppings == 1.75 or toppings == 2.5 or toppings == 3.35):
  print('The total cost of your pizza is: $ %.2f' %round((large + toppings) * tax,2))
elif (size == 'Extra' or size == 'extra') and (toppings == 1 or toppings == 1.75 or toppings == 2.5 or toppings == 3.35):
  print('The total cost of your pizza is: $ %.2f' %round((extra + toppings) * tax,2))
else :
  print('Something went wrong with your order, please try again.')
