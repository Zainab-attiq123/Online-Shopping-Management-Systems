def main():
    # Create the system
    shop = ShoppingManagementSystem()

    # --- Adding Products (Inheritance + Abstraction) ---
    print("\n📌 PILLAR 1 & 2 — ABSTRACTION + ENCAPSULATION")
    print("   (Products hide their data; abstract blueprint enforced)")
    print("-" * 62)

    p1 = ElectronicsProduct("E001", "Samsung Galaxy S24", 189999, 50, "Samsung", 2)
    p2 = ElectronicsProduct("E002", "Dell Laptop XPS 15", 329999, 20, "Dell", 3)
    p3 = ClothingProduct("C001", "Linen Kurta", 3500, 100, "L", "100% Linen")
    p4 = ClothingProduct("C002", "Denim Jeans", 5200, 75, "32", "Denim")
    p5 = FoodProduct("F001", "Organic Honey 500g", 1200, 200, "2025-12-31", True)
    p6 = FoodProduct("F002", "Basmati Rice 5kg", 1800, 150, "2026-06-30", False)

    shop.add_product(p1)
    shop.add_product(p2)
    shop.add_product(p3)
    shop.add_product(p4)
    shop.add_product(p5)
    shop.add_product(p6)

    # Demonstrate Encapsulation: validation on price/stock
    print("\n  [Encapsulation Demo] Applying discount via controlled method:")
    p1.apply_discount(10)   # ElectronicsProduct discount
    p3.apply_discount(20)   # ClothingProduct discount
    p5.apply_discount(15)   # FoodProduct discount

    # --- Registering Users (Inheritance) ---
    print("\n📌 PILLAR 3 — INHERITANCE")
    print("   (PremiumUser and AdminUser inherit from User)")
    print("-" * 62)

    u1 = User("U001", "Ahmed Khan", "ahmed@email.com")
    u2 = PremiumUser("U002", "Sara Ali", "sara@email.com", "Gold")
    u3 = AdminUser("U003", "Bilal Manager", "bilal@shop.com", "Operations")

    shop.add_user(u1)
    shop.add_user(u2)
    shop.add_user(u3)

    # --- Polymorphism Demo ---
    print("\n📌 PILLAR 4 — POLYMORPHISM")
    print("   (Same method calls, different behavior per class)")
    print("-" * 62)

    shop.display_all_products()
    shop.display_all_users()

    # --- Shopping Flow ---
    print("\n🛒 SHOPPING SIMULATION")
    print("-" * 62)

    # Customer 1 — Regular user
    print(f"\n  >> {u1.get_name()} is shopping:")
    cart1 = Cart(u1)
    cart1.add_item(p2, 1)   # Laptop
    cart1.add_item(p4, 2)   # Jeans
    cart1.add_item(p6, 3)   # Rice
    order1 = shop.checkout(cart1)
    order1.update_status("Shipped")

    # Customer 2 — Premium user
    print(f"\n  >> {u2.get_name()} is shopping (Premium):")
    cart2 = Cart(u2)
    cart2.add_item(p1, 1)   # Phone
    cart2.add_item(p3, 2)   # Kurta
    cart2.add_item(p5, 1)   # Honey
    order2 = shop.checkout(cart2)
    order2.update_status("Processing")

    # Display orders
    print("\n📋 ORDER DETAILS")
    print("-" * 62)
    shop.display_order(order1.order_id)
    shop.display_order(order2.order_id)

    # Premium user points
    print(f"\n  ⭐ {u2.get_name()} Profile after shopping:")
    print(f"  {u2.get_profile()}")

    # Review / Rating (Encapsulation)
    print("\n  [Encapsulation Demo] Adding review through controlled method:")
    p1.add_review("Excellent phone!", 5)
    p2.add_review("Great laptop for work.", 4)
    print(f"  {p1.get_name()} rating: {p1.get_rating()}/5")
    print(f"  {p2.get_name()} rating: {p2.get_rating()}/5")

    print("\n" + "=" * 62)
    print("   ✅ DEMO COMPLETE — All 4 OOP Pillars Demonstrated!")
    print("=" * 62)
    print(""" """)


if __name__ == "__main__":
    main()