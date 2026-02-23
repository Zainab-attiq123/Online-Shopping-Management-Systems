class Product(AbstractProduct):
    """
    Base Product class demonstrating ENCAPSULATION.
    Private attributes are accessed/modified only through methods.
    """

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id    # private
        self.__name = name                # private
        self.__price = price              # private
        self.__stock = stock              # private
        self.__rating = 0.0              # private
        self.__reviews = []              # private

    # --- Getters ---
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def get_rating(self):
        return self.__rating

    # --- Setters with validation ---
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price

    def set_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self.__stock = quantity

    def add_review(self, review, rating):
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        self.__reviews.append(review)
        # Recalculate average rating
        total = sum(r for r in [self.__rating] if self.__rating > 0) + rating
        self.__rating = round((self.__rating + rating) / 2 if self.__rating else rating, 1)

    def reduce_stock(self, qty):
        if qty > self.__stock:
            raise ValueError(f"Insufficient stock. Available: {self.__stock}")
        self.__stock -= qty

    def get_details(self):
        return (f"[{self.__product_id}] {self.__name} | "
                f"Price: Rs.{self.__price:.2f} | "
                f"Stock: {self.__stock} | "
                f"Rating: {self.__rating}/5")

    def apply_discount(self, percent):
        if not (0 < percent < 100):
            raise ValueError("Discount must be between 1 and 99%.")
        discount_amount = self.__price * (percent / 100)
        self.__price = round(self.__price - discount_amount, 2)
        return discount_amount

    def get_category(self):
        return "General"