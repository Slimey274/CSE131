# test_sort.py

from quicksort_module import quicksort

def test_case(name, input_list, expected_output):
    original = input_list[:]
    quicksort(input_list)
    assert input_list == expected_output, f"{name} failed.\nExpected: {expected_output}\nGot: {input_list}\nOriginal: {original}"
    print(f"{name} passed.")

def run_tests():
    test_case("Empty list", [], [])
    test_case("One element", [42], [42])
    test_case("Already sorted", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    test_case("Reversed list", [5, 4, 3, 2, 1], [1, 2, 3, 4, 5])
    test_case("Random unsorted", [3, 1, 4, 1, 5, 9, 2], [1, 1, 2, 3, 4, 5, 9])
    test_case("All same", [7, 7, 7, 7], [7, 7, 7, 7])
    test_case("Negative values", [0, -1, -3, 8], [-3, -1, 0, 8])
    test_case("Duplicates and sorted", [1, 2, 2, 2, 3], [1, 2, 2, 2, 3])

if __name__ == "__main__":
    run_tests()
