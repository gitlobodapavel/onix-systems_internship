from functools import reduce


if __name__ == "__main__":
    print("[ Warning ]: Use part4.py as module")
else:
    # Use map to print the square of each numbers rounded
    # to two decimal places
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
    print("[ Log ]: Rounded values --> " + str(list(map(lambda x: round(x * x, 2), my_floats))))

    # Use filter to print only the names that are less than
    # or equal to seven letters
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
    print("[ Log ]: Filtered names --> " + str(list(filter(lambda string: string.__len__() < 7 or string.__len__() == 7, my_names ))))

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]
    print("[ Log ]: Product of numbers --> " + str(reduce(lambda number_1, number_2: number_1 * number_2, my_numbers)))



