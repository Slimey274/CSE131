# How long did it take for you to complete this assignment?
# it took about an hour
# What was the hardest part of the assignment?
#  i feel that it was remebering how to do the algorithmic stuff.
# Was there anything unclear about the instructions or how you were to complete this lab?
# i did not think that there was any thing that was unclear to me in the homework it was farily simple.


def sort_sublist(lst, start, end):
    lst[start:end+1] = sorted(lst[start:end+1])
    return lst

def run_test_case(test_num, lst, start, end, expected):
    result = sort_sublist(lst.copy(), start, end)
    assert result == expected, f"❌ Test {test_num} failed. Expected {expected}, got {result}"
    print(f"✅ Test {test_num} passed.")

def main():
    test_cases = [
        # Test Case 1
        (1,
         [15, 3, 8, 2, 9, 7, 6, 5, 4, 1, 0, 11, 13, 14, 12, 16, 17, 18, 19, 20],
         5, 10,
         [15, 3, 8, 2, 9, 0, 1, 4, 5, 6, 7, 11, 13, 14, 12, 16, 17, 18, 19, 20]),

        # Test Case 2
        (2,
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
         0, 4,
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),

        # Test Case 3
        (3,
         [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
         10, 15,
         [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 5, 6, 7, 8, 9, 10, 4, 3, 2, 1]),

        # Test Case 4
        (4,
         [4, 6, 2, 9, 9, 3, 1, 6, 5, 5, 2, 7, 8, 9, 1, 3, 0, 4, 2, 3],
         4, 14,
         [4, 6, 2, 9, 1, 2, 3, 5, 5, 6, 7, 8, 9, 9, 9, 3, 0, 4, 2, 3]),

        # Test Case 5
        (5,
         [9, 7, 5, 3, 1, 0, 2, 4, 6, 8, 10, 11, 13, 12, 14, 15, 17, 16, 18, 19],
         0, 19,
         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    ]

    for test in test_cases:
        run_test_case(*test)

if __name__ == "__main__":
    main()
