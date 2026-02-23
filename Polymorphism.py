class Cart:
    """Shopping Cart that uses Polymorphism when handling different products."""

    def __init__(self, user):
        self.user = user
        self.__items = {}  # {product: quantity}

    def add_item(self, product, quantity=1):
        if product.get_stock() < quantity:
            print(f"  ❌ Cannot add '{product.get_name()}': insufficient stock.")
            return
        if product in self.__items:
            self.__items[product] += quantity
        else:
            self.__items[product] = quantity
        print(f"  ✅ Added {quantity}x '{product.get_name()}' to cart.")

    def remove_item(self, product):
        if product in self.__items:
            del self.__items[product]
            print(f"  🗑️  Removed '{product.get_name()}' from cart.")
        else:
            print(f"  ⚠️  Product not found in cart.")

    def display_cart(self):
        print(f"\n  🛒 Cart for: {self.user.get_name()}")
        print("  " + "-" * 60)
        if not self.__items:
            print("  Cart is empty.")
            return 0
        total = 0
        for product, qty in self.__items.items():
            # POLYMORPHISM: get_details() behaves differently for each product type
            line_total = product.get_price() * qty
            print(f"  - {product.get_name()} ({product.get_category()}) x{qty} = Rs.{line_total:.2f}")
            total += line_total
        print("  " + "-" * 60)
        print(f"  TOTAL: Rs.{total:.2f}")
        return total

    def get_items(self):
        return self.__items

    def clear(self):
        self.__items = {}


class Order:
    """Represents a placed order."""

    order_counter = 1000

    def __init__(self, user, items, total):
        Order.order_counter += 1
        self.order_id = f"ORD-{Order.order_counter}"
        self.user = user
        self.items = dict(items)
        self.total = total
        self.status = "Processing"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_status(self, status):
        valid = ["Processing", "Shipped", "Delivered", "Cancelled"]
        if status not in valid:
            print(f"  Invalid status. Choose from: {valid}")
            return
        self.status = status
        print(f"  📦 Order {self.order_id} status updated to: {self.status}")

    def display_order(self):
        print(f"\n  📋 Order ID  : {self.order_id}")
        print(f"     Customer  : {self.user.get_name()}")
        print(f"     Date/Time : {self.timestamp}")
        print(f"     Status    : {self.status}")
        print("     Items:")
        for product, qty in self.items.items():
            print(f"       • {product.get_name()} x{qty} @ Rs.{product.get_price():.2f}")
        print(f"     Total     : Rs.{self.total:.2f}")


class ShoppingManagementSystem:
    """Main system that ties everything together."""

    def __init__(self):
        self.__products = {}
        self.__users = {}
        self.__orders = {}
        print("\n" + "=" * 62)
        print("   🛍️  ONLINE SHOPPING MANAGEMENT SYSTEM  🛍️")
        print("=" * 62)

    def add_product(self, product):
        self.__products[product.get_id()] = product
        print(f"  ✅ Product added: {product.get_name()} [{product.get_category()}]")

    def add_user(self, user):
        self.__users[user.get_id()] = user
        print(f"  ✅ User registered: {user.get_name()}")

    def get_product(self, pid):
        return self.__products.get(pid)

    def get_user(self, uid):
        return self.__users.get(uid)

    def checkout(self, cart):
        items = cart.get_items()
        if not items:
            print("  ❌ Cart is empty. Cannot checkout.")
            return None
        total = cart.display_cart()
        # Reduce stock (Encapsulation: reduce_stock validates internally)
        for product, qty in items.items():
            product.reduce_stock(qty)
        order = Order(cart.user, items, total)
        self.__orders[order.order_id] = order
        cart.user.add_order(order)
        if isinstance(cart.user, PremiumUser):
            points = int(total // 100)
            cart.user.add_loyalty_points(points)
            print(f"  ⭐ {points} loyalty points added for premium member!")
        cart.clear()
        print(f"\n  🎉 Order placed successfully! Order ID: {order.order_id}")
        return order

    def display_all_products(self):
        """POLYMORPHISM: get_details() and get_category() vary per product type."""
        print("\n" + "=" * 62)
        print("   📦 ALL PRODUCTS IN STORE")
        print("=" * 62)
        for product in self.__products.values():
            # Polymorphic call — same method, different output per class
            print(f"  {product.get_details()}")
        print("=" * 62)

    def display_all_users(self):
        print("\n" + "=" * 62)
        print("   👥 REGISTERED USERS")
        print("=" * 62)
        for user in self.__users.values():
            # Polymorphic call — get_profile() differs per user type
            print(f"  {user.get_profile()}")
            # Polymorphic call — perform_action() differs per user type
            print(f"  → {user.perform_action()}")
        print("=" * 62)

    def display_order(self, order_id):
        order = self.__orders.get(order_id)
        if order:
            order.display_order()
        else:
            print(f"  ❌ Order {order_id} not found.")
