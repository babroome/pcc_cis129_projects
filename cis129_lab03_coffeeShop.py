#!/usr/bin/env python
# coding: utf-8

# In[31]:


# coffee shop code
"""generating a receipt for purchases at the coffee shop"""

#prints the initial greeting

print( )
print('***************************************')
print('My Coffee and Muffin Shop')


# In[32]:


#asks user for number of products purchased

coffees = int(input('Number of coffees bought?\n'))
muffins = int(input('Number of muffins bought?\n'))
teas = int(input('Number of teas bought?\n'))
bagels = int(input('Number of bagels bought?\n'))

# In[33]:


#assigns variables for products and prices

coffee_price = (5.00)
muffin_price = (4.00)
tea_price = (3.00)
bagel_price = (3.50)

coffee_total = coffees * coffee_price
muffin_total = muffins * muffin_price
tea_total = teas * tea_price
bagel_total = bagels * bagel_price

subtotal = coffee_total + muffin_total + tea_total + bagel_total
sales_tax = subtotal * (.06)
total = subtotal + sales_tax


# In[34]:


#prints total receipt with total charges

print( )
print('***************************************\n') 
print('***************************************\n')

print('My Coffee and Muffin Shop Receipt')

print(coffees,'coffees at $5 each: ${:.2f}'.format(coffee_total))
print(muffins,'muffins at $5 each: ${:.2f}'.format(muffin_total))
print(teas,'teas at $3 each: ${:.2f}'.format(tea_total))
print(bagels,'bagels at $3.50 each: ${:.2f}'.format(bagel_total))

print('6% sales tax: ${:,.2f}'.format(sales_tax))
print('---------')
print('Total: ${:,.2f}'.format(total))

print( )
print('***************************************\n')


# In[ ]:




