

def convert_binary(number):
    '''Conver the Intger number to binary'''
    return "0b11"

def convert_octal(number):
    '''COnver the integer number to Octal'''
    return "o357"

def convert_hex(number):
    '''Conver the integer number to hexadecimal'''
    return "0xF3"

def conversion(number):
    '''Dirver function for the convert functions'''
    binary = convert_binary(number)
    octal = convert_octal(number)
    hex = convert_hex(number)\
    
    return binary, octal, hex

def output_numbers(number, binary, octal, hex):
    "Format output for the converted functions"
    assert type(number) == int
    assert type(binary) == str
    assert type(octal) == str
    assert type(hex) == str

    print(f"Number: {number:10} Binary: {binary:>10} Octal: {octal:>10} Hex: {hex:>10}")

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

def main():
    number = get_number()
    print(f'Got a good number {number}')
    binary, octal, hex = conversion(number)
    output_numbers(number, binary, octal, hex)

main()