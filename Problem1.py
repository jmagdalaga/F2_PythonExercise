cel = float(input("Enter the Celsius: "))

fah = (cel * 9 / 5) + 32

int_num = int(fah)
dec = (fah - int_num) * 100

dec_rounded = int(dec + 0.5)
if dec_rounded >= 100:
    int_num += 1
    dec_rounded = 0

print(f"{cel} ° Celsius is equal to {int_num}.{dec_rounded:02d} ° Fahrenheit")

