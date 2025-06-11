
def display_names(names):
    for name in names:
        print(name)


def display_names_recursive(names):
    if not names:
        return
    else:
        print(names[0], end = ' ')
        display_names_recursive(names[1:])

def display_names_r2(names, names_length):
    if names_length == 0:
        return
    else:
        print(names[names_length], end = ' ')
        return display_names_r2(names, names_length - 1)

def main():
    names = ['Adam', 'Bob', 'Charles', 'Doug', 'Eddie']
    display_names(names)
    print()
    display_names_recursive(names)
    print()
    names_length = len(names)
    display_names_r2(names , names_length - 1)
    
main()