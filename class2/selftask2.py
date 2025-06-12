tip=int(input("Enter your tip %: 15, 18, 20 or more "))

if tip == 15:
    print(f"standard")
elif tip == 18:
    print(f"good")
elif tip == 20:
    print(f"great")
elif tip > 20:
    print(f"my hero")
else:
    print("wrong number")