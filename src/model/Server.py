
from model.User import User


class Server:
    """
    TODO: Class for defining attributes and methods of servers.
    """
    amount = 0
    
    def __init__(self, ttask, umax):
        self.users_connected = []
        self.cost_value = 0
        self.ttask = ttask
        self.umax = umax

    def connect_user(self):
        new_user = User()
        self.users_connected.append(new_user)

    def disconnect_user(self, user):
        self.users_connected.remove(user)

    def setCostValue(self):
        self.__class__.amount += self.cost_value

    def getUsers(self):
        return len(self.users_connected)

    def __repr__(self):
        return str(len(self.users_connected))

    def check_tick_in_users(self):
        """
        TODO: Check quantity and add tick for all users.
        """
        remove_users = []

        for user in self.users_connected:
            if user.getTick() >= self.ttask:
                remove_users.append(user)
            else:
                user.setTick()

        for remove_user in remove_users:
            self.disconnect_user(remove_user)

    @classmethod
    def total_cost(cls):
        """
        Return total cost for all active servers.
        """
        return str(cls.amount)