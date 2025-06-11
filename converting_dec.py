

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
    print(number, binary, octal, hex)

def get_number():
    '''Obtains number from user'''
    return 10

def test_conversions():
    '''Tests for the conversion functions'''
    pass

def main():
    number = get_number()
    binary, octal, hex = conversion(number)
    output_numbers(number, binary, octal, hex)

main()