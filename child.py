from parent import Parent


class Child(Parent):

    def __init__(self, number, variable):
        self.__protected_variable = variable
        super().__init__(number)

        print("[ Log ]: result of __protected_child__class_method() --> " + str(self.__protected_child_class_method(self.__protected_variable)))

    def __del__(self):
        """Message to display when object is removed"""
        print("[ Log ]: Child class object has been removed")

    def set_variable(self, var):
        self.__protected_variable = var

    def get_variable(self):
        return self.__protected_variable

    def __protected_child_class_method(self, variable):
        return type(variable) is str