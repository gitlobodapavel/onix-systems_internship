class Parent:
    def __init__(self, number):
        """Initialization parameters"""
        self.number = number

    def __del__(self):
        """Message to display when object is removed"""
        print("[ Log ]: Parent class object has been removed")

    def is_divisible_by(self, divided, divider):
        return divided % divider == 0

    @staticmethod
    def parent_static_method(num_1, num_2):
        anonimous_method = lambda x, y: x * y
        return anonimous_method(num_1, num_2)
