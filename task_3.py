

def secondTask():
    # 1 variables

    print("-" * 10 + " Variables " + "-" * 10)

    num_var = 1
    string_var = "1"
    print("[ Log ]: Variable num_var has type: " + str(type(num_var)))
    print("[ Log ]: Variable string_var has type: " + str(type(string_var)))

    print("[ Log ]: Converting num to sting type...")
    num = str(num_var)
    print("[ Log ]: Variable num_var has type: " + str(type(num)))

    # 2 lists

    print("-" * 10 + " Lists " + "-" * 10)

    list = [1, 4, 8, 8]
    print("[ Log ]: Created list: " + str(list))
    list.append(5)
    print("[ Log ]: Appended 5 to list --> list: " + str(list))
    list.insert(2, 9)
    print("[ Log ]: Inserted '2' element to list --> list: " + str(list))
    list.pop(0)
    print("[ Log ]: Removed '0' element of list --> list: " + str(list))
    list.pop(2)
    print("[ Log ]: Removed '2' element of list --> list: " + str(list))
    list.reverse()
    print("[ Log ]: Reversed list --> list: " + str(list))
    list_len = list.__len__()
    print("[ Log ]: The length of list: " + str(list_len))
    list_copy = list

    list_copy.sort()
    print("[ Log ]: Sorted list (.sort()): " + str(list_copy))

    print("-" * 10 + " Strings " + "-" * 10)

    string = "This is a test string for Internship Onix for python"

    print("[ Log ]: String to sort: " + string)


    print("-" * 10 + " Dicts " + "-" * 10)

    dict = {
        'Name': 'Pavel',
        'Surname': 'Loboda',
        'City': 'Kirovograd',
        'Country': 'Ukraine'
    }
    print("[ Log ]: Created dictionary: " + str(dict))

    dict['Age'] = '17'

    print("[ Log ]: Added Age element: " + str(dict))

    age = dict['Age']

    print("[ Log ]: Age: " + age)

    del dict['Age']

    print("[ Log ]: Removed Age element: " + str(dict))

    print("[ Log ]: Keys: " + str(dict.keys()))
    print("[ Log ]: Values: " + str(dict.values()))

def multiplication(vars_list, factor):
    vars_list.append(factor * global_variable)
    return vars_list, vars_list.__len__()

def printArguments(*args, **kwargs):
    print("[ Log ]: Args: " + str(args) + "\n" + "[ Log ]: Kwargs: " + str(kwargs))

def is_divisible_by_num(devided, devider):
    return devided % devider == 0


def fibo(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fibo(number-1) + fibo(number-2)

def get_fibonacci_list():
    fibo_list = []
    for i in range(25):
        fibo_list.append(fibo(i))
        i = i + 1
    return fibo_list

def main():
    if __name__ == "__main__":
        secondTask()

        vars_list = []

        vars_list, vars_list_len = multiplication(vars_list, 2)
        vars_list, vars_list_len = multiplication(vars_list, 4)
        vars_list, vars_list_len = multiplication(vars_list, 6)

        print("[ Log ]: List of multiplied variables: "+str(vars_list) + "\n" + "[ Log ]: Length of the list: " + str(vars_list_len))

        printArguments(12, True, 3.14, "String", name="Pavel", surname="Loboda", age="17")

        print("20 \ 5 is divides without trace: " + str(is_divisible_by_num(24, 5)))

        print("[ Log ]: Fibonacci list (0 - 25)")

        print(get_fibonacci_list())

global_variable = 10

main()