from tesgtbed3 import my2ndclass


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


    shitty = my2ndclass(20)
    shitty.showfromclass(shitty)
    crappy = my2ndclass(10)
    crappy.showfromclass(crappy)
    my2ndclass.share2 += 1000
    print(shared_variable)
    print(my2ndclass.share2)
    crappy.showfromclass(crappy)
