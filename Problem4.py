num = int(input("Enter an integer: "))
res = 0

if num < 1:
    print("Please enter a positive integer.")
else:
    i = 1
    while i <= num:
        res += i
        i += 1
    print(f"The sum of all numbers from 1 to {num} is: {res}")
