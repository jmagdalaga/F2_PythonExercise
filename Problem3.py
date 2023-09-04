n = int(input("Please enter a number: "))

count = 0
s_num = 9
h_num = 0

if n < 0:
    n = -n

temp_num = n
while temp_num > 0:
    digit = temp_num % 10
    count += 1

    if digit < s_num:
        s_num = digit
    if digit > h_num:
        h_num = digit

    temp_num //= 10

print(f"Number of digits in the given number is: {count}")
print(f"Smallest number is: {s_num}")
print(f"Highest number is: {h_num}")
