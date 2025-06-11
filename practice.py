
def getTemputure():
    fahrenehit = float(input("Please enter in the tempruture in fahrenehit: "))
    return fahrenehit

def convert(fahrenehit):
    celcius =  (5 / 9) * (fahrenehit -32)
    return celcius

def convert(celcius):
    kelvin = celcius + 273.15
    return kelvin
     
def display(celcius, kelvin):
        print(f"The temptuture of celscius: {celcius: .2f}")
        print(f"The tempruture of Kelvin: {kelvin: .2f}")

def main():
    fahrenehit = getTemputure()
    celcius = convert(fahrenehit)
    kelvin = convert(celcius)
    display(celcius, kelvin)
main()