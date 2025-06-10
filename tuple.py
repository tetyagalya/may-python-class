
foods=("burger", "pizza", "taco")
drinks=("coke","pepsi","juice")
print(f"Can i get {foods[2]}, and {drinks[-1]}?")

foods.append("sushi")
print(foods)

#cannot use append and extend in tuple 

# ^^ if i'd like to print only one value from tuple, can use drinks=("coke","pepsi","juice")next line -> print(drinks[1])
#if we count from right to left, then 1st element is -1, next -2, etc.
