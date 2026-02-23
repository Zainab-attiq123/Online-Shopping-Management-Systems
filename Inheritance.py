lass ElectronicsProduct(Product):
    """
    INHERITANCE: Inherits from Product and adds Electronics-specific fields.
    """

    def __init__(self, product_id, name, price, stock, brand, warranty_years):
        super().__init__(product_id, name, price, stock)
        self.brand = brand
        self.warranty_years = warranty_years

    def get_details(self):
        base = super().get_details()
        return f"{base} | Brand: {self.brand} | Warranty: {self.warranty_years} yr(s)"

    def get_category(self):
        return "Electronics"

    def apply_discount(self, percent):
        amount = super().apply_discount(percent)
        print(f"  Electronics discount applied! You save Rs.{amount:.2f}")
        return amount


class ClothingProduct(Product):
    """
    INHERITANCE: Inherits from Product and adds Clothing-specific fields.
    """

    def __init__(self, product_id, name, price, stock, size, material):
        super().__init__(product_id, name, price, stock)
        self.size = size
        self.material = material

    def get_details(self):
        base = super().get_details()
        return f"{base} | Size: {self.size} | Material: {self.material}"

    def get_category(self):
        return "Clothing"

    def apply_discount(self, percent):
        amount = super().apply_discount(percent)
        print(f"  Seasonal clothing discount applied! You save Rs.{amount:.2f}")
        return amount


class FoodProduct(Product):
    """
    INHERITANCE: Inherits from Product and adds Food-specific fields.
    """

    def __init__(self, product_id, name, price, stock, expiry_date, is_organic):
        super().__init__(product_id, name, price, stock)
        self.expiry_date = expiry_date
        self.is_organic = is_organic

    def get_details(self):
        base = super().get_details()
        organic_tag = "Organic" if self.is_organic else "Regular"
        return f"{base} | Expiry: {self.expiry_date} | Type: {organic_tag}"

    def get_category(self):
        return "Food"

    def apply_discount(self, percent):
        amount = super().apply_discount(percent)
        print(f"  Flash food sale! You save Rs.{amount:.2f}")
        return amount