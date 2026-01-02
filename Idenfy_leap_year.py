year=int(input("Enter the Year: "))

# There are two condition for identify the leap year
if year%400==0:
    print("This year is leap year")

elif year%4==0 and year%100!=0:
    print("This year is leap year")

# if both condition are False than run this condition
else:
    print("This is not a leap year") 

    

