class my2ndclass:

    share2 = 12344
    varieed = "a"


    def __init__(self,valre):
        self.apes = valre
        self.testing = "I tried"

    def showfromclass(self,varidd):
        my2ndclass.varieed = varidd
        print("test")
        print(f"shitman {varidd}")
        varidd.theprint()
        print(my2ndclass.share2)


    def theprint(self):
        print("test2")
        print(self.apes)
        print(f"from inside class {my2ndclass.share2}")
        print(self.testing)


