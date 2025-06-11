# 1. Name:
#      -Briant Woolley-
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-



def display_table(week, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(week) == type(0))
    assert(0 <= week <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(week):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        week += 1
        # Newline after Saturdays
        if week % 7 == 0:
            print("") # newline

    # We must end with a newline
    if week % 7 != 0:
        print("") # newline

def leap_year(year):
    '''Check if year is leap year'''
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0)

def get_days_in_month(month, year):
    if month == 2:
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def count_days_since_1753(month, year):
    total_days = 0

    for y in range(1753, year):
        total_days += 366 if leap_year(y) else 365

    for m in range(1, month):
        total_days += get_days_in_month(m, year)

    return total_days

def main():
    month = int(input("Enter the month number: "))
    year = int(input("Enter year: "))

    # Basic validation
    if not (1 <= month <= 12) or year < 1753:
        print("Invalid input.")
        return

    # Output
    num_days = get_days_in_month(month, year)
    total_days = count_days_since_1753(month, year)
    week = (total_days + 1) % 7  # Jan 1, 1753 was a Monday, which is dow=1

    display_table(week, num_days)

main()