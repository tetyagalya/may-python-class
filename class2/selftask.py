age=int(input("Enter your age: "))

if age < 13:
    print(f"you are a child")
elif age >= 13 and age < 18:
    print(f"you are a teenager")
elif age >= 18 and age < 65:
    print(f"you are an adult")
elif age >= 65:
    print(f"you are an elder")
else:
    print(f"wrong age")