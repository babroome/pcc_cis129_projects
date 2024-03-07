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


# In[33]:


#assigns variables for products and prices

coffee_price = (5.00)
muffin_price = (4.00)

coffee_total = coffees * coffee_price
muffin_total = muffins * muffin_price

subtotal = coffee_total + muffin_total
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
print('6% sales tax: ${:,.2f}'.format(sales_tax))
print('---------')
print('Total: ${:,.2f}'.format(total))

print( )
print('***************************************\n')


# In[ ]:




