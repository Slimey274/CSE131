

def convert_binary(number):
    '''Convert the Intger number to binary'''
    if number == 0:
        return "0"
    
    binary_digits = []
    while number > 0:
        binary_digits.append(str(number %2))
        number = number // 2

    binary_digits.reverse()
    binary_string = ''.join(binary_digits)
    return "0b" + binary_string

def convert_octal(number):
    '''Convert the integer number to Octal'''
    if number == 0:
        return "0"
    
    octal_digits = []
    while number > 0:
        octal_digits.append(str(number % 8))
        number = number // 8

    octal_digits.reverse()
    octal_string = ''.join(octal_digits)
    return "0o" + octal_string


def convert_hex(number):
    '''Convert the integer number to hexadecimal'''
    if number == 0:
        return "0"
    
    hex_digits = []

    hex_string = ''

    while number > 0:
        hex_digits.append(number % 16)
        number //= 16
    
    hex_letters = ['A', 'B', 'C', 'D', 'E', 'F']
    return "0xF3"

def conversion(number):
    '''Dirver function for the convert functions'''
    binary = convert_binary(number)
    octal = convert_octal(number)
    hex = convert_hex(number)
    
    return binary, octal, hex

def output_numbers(number, binary, octal, hex):
    "Format output for the converted functions"
    assert type(number) == int
    assert type(binary) == str
    assert type(octal) == str
    assert type(hex) == str

    print(f"Number: {number:5} \nBinary: {binary:>5} \nOctal: {octal:>5} \nHex: {hex:>5}")

def get_number():
    '''Obtains number from user'''
    number = -1
    while number < 0:
        try:
            number = int(input('Please enter in a Positive number: '))
            if number < 0:
                raise TypeError
        except (ValueError, TypeError, KeyboardInterrupt, EOFError):
            print('Invalid number please try again.')

    return number

def test_conversions():
    '''Tests for the conversion functions'''
    pass

def test_convert_binary():
    assert convert_binary(255) == "0b11111111"
    assert convert_binary(1) == "0b1"
    assert convert_binary(128) == "0b10000000"
    print("Binary tests complete")

def test_convert_octal():
    assert convert_octal(255) == "0o377"
    assert convert_octal(25) == "0o31"
    assert convert_octal(128) == "0o200"
    print("Octal tests pass")

def main():
    test_convert_binary()
    test_convert_octal()
    number = get_number()
    print(f'Got a good number {number}')
    binary, octal, hex = conversion(number)
    output_numbers(number, binary, octal, hex)

main()