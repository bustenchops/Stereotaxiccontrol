class testsends:

    def __init__(self):
        self.iliketomoveit = "none"

    def receive_instance(self, maininstance):
        self.iliketomoveit = maininstance

    def changevar(self):
        self.iliketomoveit.canyousee()
        self.iliketomoveit.handle_signal()