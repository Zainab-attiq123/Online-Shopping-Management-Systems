class User(AbstractUser):
    """Base User class with Encapsulation and Abstraction."""

    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self._orders = []

    def get_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def add_order(self, order):
        self._orders.append(order)

    def get_orders(self):
        return self._orders

    def get_profile(self):
        return f"User [{self.__user_id}]: {self.__name} | Email: {self.__email}"

    def perform_action(self):
        return f"{self.__name} is browsing the shop."


class PremiumUser(User):
    """
    INHERITANCE: Premium users get extra benefits.
    """

    def __init__(self, user_id, name, email, membership_level):
        super().__init__(user_id, name, email)
        self.membership_level = membership_level
        self.__loyalty_points = 0

    def add_loyalty_points(self, points):
        self.__loyalty_points += points

    def get_loyalty_points(self):
        return self.__loyalty_points

    def get_profile(self):
        base = super().get_profile()
        return f"{base} | Membership: {self.membership_level} | Points: {self.__loyalty_points}"

    def perform_action(self):
        return f"{self.get_name()} (Premium) is shopping with exclusive benefits."


class AdminUser(User):
    """
    INHERITANCE: Admin users manage the system.
    """

    def __init__(self, user_id, name, email, department):
        super().__init__(user_id, name, email)
        self.department = department

    def get_profile(self):
        base = super().get_profile()
        return f"{base} | Role: Admin | Dept: {self.department}"

    def perform_action(self):
        return f"{self.get_name()} (Admin) is managing the system."
