year=int(input("Enter number of years: "))
unit=input(""""pick a choice: 
1-days 
2-weeks
3-hours
What is your choice? """)

if unit == "1":
    print(f"in {year} years {year*365} days")
elif unit ==  "2":
    print(f"in {year} years {year*52} weeks")
elif unit == "3":
    print(f"in {year} years {year*365*24} hours")
else:
    print("wrong choice")