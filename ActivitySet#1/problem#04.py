# Conditional Execution

hrs =float(input("Enter Hours:\n"))
rate=float(input("Enter the rate per hour:\n"))
if hrs<=40:
    print("gross pay= ",(hrs*rate))
else:
    print((40*rate)+((hrs-40)*rate*1.5))
          
