import copy

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],               "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

categories = ["Starters", "Mains", "Desserts"]
for cat in categories:
    print(f"\n===== {cat} =====")
    for item, details in menu.items():
        if details["category"] == cat:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{item} - {details['price']} - {status}")

total_items = len(menu)
available_items = 0
for item in menu.values():
    if item["available"]:
        available_items += 1

most_expensive_name = ""
highest_price = 0
for name, details in menu.items():
    if details["price"] > highest_price:
        highest_price = details["price"]
        most_expensive_name = name

most_expensive = (most_expensive_name, {"price": highest_price})
cheap_items = []
for name, details in menu.items():
    if details["price"] < 150:
        item_info = name + " (" + str(details["price"]) + ")"
        cheap_items.append(item_info)

print("\nTotal Items: ", total_items)
print("Total Available:", available_items)
print("Most Expensive:", most_expensive)
print("Cheap items:", cheap_items)





cart = []
def add_to_cart(name, qty):
    print(f"\nAttempting to add: {name} x{qty}")
    if name not in menu:
        print(f"Error: '{name}' does not exist in menu.")
    elif not menu[name]["available"]:
        print(f"Error: '{name}' is currently unavailable.")
    else:
        found = False
        for entry in cart:
            if entry["item"] == name:
                entry["quantity"] += qty
                found = True
        if not found:
            new_item = {"item": name, "quantity": qty, "price": menu[name]["price"]}
            cart.append(new_item)
    print("Current Cart List:", cart)

def remove_from_cart(name):
    for i in range(len(cart)):
        if cart[i]["item"] == name:
            cart.pop(i)
            print(f"\nRemoved {name} from cart.")
            break
    print("Current Cart List:", cart)

add_to_cart("Paneer Tikka", 2)
add_to_cart("Gulab Jamun", 1)
add_to_cart("Paneer Tikka", 1)
add_to_cart("Mystery Burger", 1) 
add_to_cart("Chicken Wings", 1)  
remove_from_cart("Gulab Jamun")

print("\n========== Order Summary ==========")
subtotal = 0
for entry in cart:
    item_total = entry["quantity"] * entry["price"]
    subtotal += item_total
    print(f"{entry['item']} x{entry['quantity']} - ₹{item_total}")

gst = subtotal * 0.05
total = subtotal + gst
print("------------------------------------")
print(f"Subtotal: ₹{subtotal}")
print(f"GST (5%): ₹{gst}")
print(f"Total Payable: ₹{total}")
print("====================================")



inventory_backup = copy.deepcopy(inventory)
original_val = inventory["Paneer Tikka"]["stock"]
inventory["Paneer Tikka"]["stock"] = 0 
print(f"Live Inventory (Modified): {inventory['Paneer Tikka']['stock']}")
print(f"Backup Inventory (Original): {inventory_backup['Paneer Tikka']['stock']}")
inventory["Paneer Tikka"]["stock"] = original_val
print("Inventory Restored.")

for entry in cart:
    name, qty = entry["item"], entry["quantity"]
    if name in inventory:
        current = inventory[name]["stock"]
        if qty > current:
            print(f"⚠ Warning: Insufficient stock for {name}.")
            inventory[name]["stock"] = 0
        else:
            inventory[name]["stock"] = current - qty

print("\n--- Reorder Alerts ---")
for item, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} - Only {data['stock']} unit(s) left (reorder level: {data['reorder_level']})")

print("\n--- Final Verification ---")
print("Final Live Inventory State (Modified by Cart):")
print(inventory["Paneer Tikka"])
print("\nFinal Backup Inventory State (Original):")
print(inventory_backup["Paneer Tikka"])



sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

daily_revenue = {}
item_counts = {}
all_orders_list = [] 

for date, orders in sales_log.items():
    day_total = 0
    for order in orders:
        day_total += order["total"]
        all_orders_list.append({"date": date, "order": order})
        for item in order["items"]:
            item_counts[item] = item_counts.get(item, 0) + 1
    daily_revenue[date] = day_total

print("\nRevenue per Day:")
for date, rev in daily_revenue.items():
    print(f"{date}: ₹{rev}")

best_day = max(daily_revenue, key=daily_revenue.get)
print(f"\nBest-selling Day: {best_day} (₹{daily_revenue[best_day]})")

most_ordered_item = max(item_counts, key=item_counts.get)
print(f"Most Ordered Item: {most_ordered_item} ({item_counts[most_ordered_item]} orders)")

print("\nFull Order List:")
for index, entry in enumerate(all_orders_list, 1):
    d, o = entry["date"], entry["order"]
    items_str = ", ".join(o["items"])
    print(f"{index}. [{d}] Order #{o['order_id']} — ₹{o['total']} — Items: {items_str}")