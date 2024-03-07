# coffee shop code
"""generating a receipt for purchases at the coffee shop"""

print( )
print('***************************************')
print('My Coffee and Muffin Shop')

coffees = int(input('Number of coffees bought?\n'))
muffins = int(input('Number of muffins bought?\n'))

coffee_price = (5.00)
muffin_price = (4.00)

coffee_total = coffees * coffee_price
muffin_total = muffins * muffin_price

subtotal = coffee_total + muffin_total
sales_tax = subtotal * (.06)
total = subtotal + sales_tax

print( )
print('***************************************\n')
#print( )      
print('***************************************\n')
#print( )     
print('My Coffee and Muffin Shop Receipt')
print(coffees,"coffees at $5 each: $", coffee_total)
print(muffins,"muffins at $5 each: $", muffin_total)
print('6% sales tax:', sales_tax)
print('Total: $', total)
