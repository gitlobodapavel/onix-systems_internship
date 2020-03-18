from parent import Parent
from child import Child
from child2 import SecondChild
import part4

if __name__ == "__main__":
    # Part 1
    parent_class_obj = Parent(100)
    print("[ Log ]: result of is_divisible_by() method --> " + str(parent_class_obj.is_divisible_by(100, 10)))
    print("[ Log ]: result of parent_static_method() --> " + str(parent_class_obj.parent_static_method(100, 10)))

    # Part 2
    child_class_object = Child(100, "String")
    print("[ Log ]: result of is_divisible_by() method (IN CHILD CLASS) --> " + str(child_class_object.is_divisible_by(100, 10)))

    try:
        print(child_class_object.__variable)
    except:
        print("[ Log ]: Can`t call the private variable")

    # Part 3
    second_child_class_obj = SecondChild(100, "String")
    second_child_class_obj.parent_static_method(120, 33)

else:
    print("[ Warning ]: Run this code as individual script (NOT MODULE)")