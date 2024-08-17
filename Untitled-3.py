
no = int(input("Enter your mark: "))

if no > 0:
    if no % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
elif no < 0:
    print("The number is negative")
else:
    print("The number is zero")
