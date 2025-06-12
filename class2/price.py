#spend 100$ and more and get 10% discount
#if we buy for 80$ - we pay 80$
#if we buy for 150$ - we pay $135
#we pay 10% tax 

discount=0
sales_tax=0.1

def tax_func(price):     #tax price
    taxes = price * sales_tax
    return taxes

def discount_func(price, discount): 
    discount_sum = price * (discount / 100)
    return discount_sum

price=float(input("enter price: "))
tax=tax_func(price)

if price > 100 and price <= 200:  #if price 101-200, then discount sum=price*0.1
   discount = discount_func(price, 10)
elif price > 200:    #if price > 200,, the discount price is discount sum=price*0.2
   discount = discount_func(price, 20)

total_price = price + tax - discount 

print(total_price)

#discount=10%
#price=100
#100*(10/100)

 #important thing is to define the starting point. always think, what is your starting point? from where we start - always think