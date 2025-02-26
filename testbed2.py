class MyClass:
    # Class variable
    shared_variable = 0

    def __init__(self, value):
        # Instance variable
        self.instance_variable = value

    def increment_shared_variable(self):
        MyClass.shared_variable += 1

    def display_variables(self):
        print(f"Instance Variable: {self.instance_variable}")
        print(f"Shared Variable: {MyClass.shared_variable}")

# Create instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

# Increment the shared variable using obj1
obj1.increment_shared_variable()

# Display variables for both objects
obj1.display_variables()
obj2.display_variables()

# Increment the shared variable using obj2
obj2.increment_shared_variable()

# Display variables again to see the change
obj1.display_variables()
obj2.display_variables()