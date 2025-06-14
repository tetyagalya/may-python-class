while True:
    age=int(input("Enter your age: "))
    
    if age > 0 and age < 13:
        print ("Sorry you're not allowed to pass")
    elif age >= 13 and age < 18:
        print ("Please call your legal guardian")
    elif age >= 18:
        print ("Welcome")
    else:
        print("provide right age")

