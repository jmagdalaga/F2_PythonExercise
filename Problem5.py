def decToBinary(dec):
    if dec == 0:
        return '0'

    binary = ''
    while dec > 0:
        remainder = dec % 2
        binary = str(remainder) + binary
        dec //= 2

    return binary

def binaryToN(binary, base):
    if base not in (2, 8, 16):
        return "Invalid base"

    result = 0
    binary_length = len(binary)
    power = 0
    i = binary_length - 1
    while i >= 0:
        digit = int(binary[i])
        result += digit * (base ** power)
        power += 1
        i -= 1

    return result

def decToOctal(dec):
    if dec == 0:
        return '0'

    octal = ''
    while dec > 0:
        remainder = dec % 8
        octal = str(remainder) + octal
        dec //= 8

    return octal

def decToHex(dec):
    if dec == 0:
        return '0'

    hex_chars = '0123456789ABCDEF'
    hex_value = ''

    while dec > 0:
        remainder = dec % 16
        hex_value = hex_chars[remainder] + hex_value
        dec //= 16

    return hex_value

def reverseString(string):
    reversed_str = ''
    i = len(string) - 1
    while i >= 0:
        reversed_str += string[i]
        i -= 1
    return reversed_str

def main():
    dec_num = 42  # Choose any decimal number you want

    print(f"Decimal: {dec_num}")

    bin_val = decToBinary(dec_num)
    print(f"Binary: {bin_val}")

    oct_val = decToOctal(dec_num)
    print(f"Octal: {oct_val}")

    hex_val = decToHex(dec_num)
    print(f"Hexadecimal: {hex_val}")

    # Now, let's convert binary back to decimal using binaryToN function
    con_dec = binaryToN(reverseString(bin_val), 2)
    print(f"Converted Binary to Decimal: {con_dec}")


if __name__ == "__main__":
    main()
