class my2ndclass:

    share2 = 12344

    def __init__(self,valre):
        self.apes = valre

    def showfromclass(self,varidd):
        self.varieed = varidd
        print("test")
        varidd.theprint()


    def theprint(self):
        print("test2")
        print(self.apes)
        print(f"from inside class {my2ndclass.share2}")


