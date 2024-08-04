class MyClass:
    class_variable = 0

    def __init__(self):
        self.instance_variable = 10

    def change_class_variable(self, new_value):
        MyClass.class_variable = new_value

# Create two instances
obj1 = MyClass()
obj2 = MyClass()

# Access the class variable before modification
print(obj1.class_variable)
print(obj2.class_variable)

# Modify the class variable using an instance
obj1.change_class_variable(5)

# Access the class variable after modification
print(obj1.class_variable)
print(obj2.class_variable)