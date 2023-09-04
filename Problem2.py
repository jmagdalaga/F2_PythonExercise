int_num1 = int(input("First integer: "))
int_num2 = int(input("Second integer: "))
int_num3 = int(input("Third integer: "))

maximum = int_num1

if int_num2 > maximum:
    maximum = int_num2

if int_num3 > maximum:
    maximum = int_num3

print(f"The maximum number among the three is {maximum}.")
