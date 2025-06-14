#0 1 1 2 3 5 8 13 21 34 55 89 

#pls  print fibonacci sequence (the most common Q in the interviews)

limit=int(input("Enter limit: "))
first=0
second=1
print(first)
print(second)
next = first + second 

while next < limit:
    print(next)
    first=second
    second=next
    next = first + second 

#we know 1st and 2d numbers 
#limit=200

# while 1<2 never ending loop, cuz 1 is always less than 2 
# or while true (also never ending loop)
