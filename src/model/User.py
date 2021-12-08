
class User:
    """
    TODO: Class for defining attributes and methods of users.
    """
    tick = 0

    def setTick(self):
        self.tick += 1

    def getTick(self):
        return self.tick

    def __repr__(self):
        return f"Tick: {self.tick}"