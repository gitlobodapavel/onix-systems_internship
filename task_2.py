def bubbleSort(list):

    for i in range(list.__len__() - 1):
        for c in range(list.__len__() - 1):
            if list[c] > list[c + 1]:

                element_1 = list[c]
                element_2 = list[c + 1]

                list[c] = element_2
                list[c + 1] = element_1

    return list

def keysSort(dict):

    print("[ Log: ] Sorting by keys:")

    dict_keys = list(dict.keys())
    dict_keys.sort()
    print("\n[")
    for i in dict_keys:
        print("    " + i + " --> " + dict[i])
    print("]")

def valSort(dict):
    print("[ Log: ] Sorting by keys:")

    dict_values = list(dict.items())
    dict_values.sort(key=lambda i: i[1])
    print("\n[")
    for i in dict_values:
        print("    " + i[0] + " --> " + i[1])
    print("]")


def alphabetSort(_string):
    string_list = _string.split()
    return sorted(string_list)

def main():
    # 1 variables

    print("-" * 10 + " Variables " + "-" * 10)

    num_var = 1
    string_var = "1"
    print("[ Log ]: Variable num_var has type: "+str(type(num_var)))
    print("[ Log ]: Variable string_var has type: " +str(type(string_var)))

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

    list = bubbleSort(list)
    print("[ Log ]: Sorted list (BubbleSort): " + str(list))

    list_copy = sorted(list_copy)
    print("[ Log ]: Sorted list (sorted(): " + str(list_copy))

    print("-" * 10 + " Strings " + "-" * 10)

    string = "This is a test string for Internship Onix for python"

    print("[ Log ]: String to sort: " + string)

    list_sorted = alphabetSort(string.lower())
    string_sorted = ' '.join(list_sorted)
    print("[ Log ]: Sorted string: " + string_sorted)

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

    keysSort(dict)

    valSort(dict)

main()