from child import Child


class SecondChild(Child):
    def __init__(self, number, variable):
        super().__init__(number, variable)

    def __del__(self):
        """Message to display when object is removed"""
        print("[ Log ]: SecondChild class object has been removed")


    @staticmethod
    def parent_static_method(number_1, number_2):
        """Redefinition of parent method"""

        """Counting GCD"""

        if number_1 > number_2:
            smaller = number_2
        else:
            smaller = number_1
        for i in range(1, smaller + 1):
            if ((number_1 % i == 0) and (number_2 % i == 0)):
                gcd = i

        print("[ Log ]: GCD( " + str(number_1) + " and "+str(number_2) + " ) --> " + str(gcd))

        """Counting LCM"""

        if number_1 > number_2:
            smaller = number_1
        else:
            smaller = number_2

        while (True):
            if ((smaller % number_1 == 0) and (smaller % number_2 == 0)):
                lcm = smaller
                break
            smaller += 1

        print("[ Log ]: LCM( " + str(number_1) + " and "+str(number_2) + " ) --> " + str(lcm))

