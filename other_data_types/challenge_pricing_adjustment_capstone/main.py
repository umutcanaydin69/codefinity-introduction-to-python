grocery_inventory = {"Milk": ("Dairy", 3.50, 8),
                    "Eggs": ("Dairy", 5.50, 30),
                    "Bread": ("Bakery", 2.99, 15),
                    "Apples": ("Produce", 1.50, 50)}
category, price, stock = grocery_inventory["Eggs"]
if price > 5:  
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (category, price - 1, stock)
else:
    print("Thre price of Eggs is reasonable.")

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes: ", grocery_inventory)
category, price, milk_stock = grocery_inventory["Milk"]

if milk_stock < 10:
    grocery_inventory["Milk"] = (category, price, milk_stock + 20)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

category, price, stock = grocery_inventory["Apples"]

if price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("Updated inventory: ", grocery_inventory)

