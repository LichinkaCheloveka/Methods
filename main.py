from Methods import bisection_method, golden_ratio, fibonacci, search_minimal_segment
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc_number, result = fibonacci(0, 1,  0.1, "fibonacci.txt")
    search_minimal_segment(1, 10E-3, "search_minimum.txt")
    print(calc_number, result)
