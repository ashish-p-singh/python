item=input("Enter item name: ")
price=float(input("Enter item price: "))
quantity=int(input("Enter item quantity: "))
currency="$"
total=price*quantity
print(f"You have purchased {item} at {price} {quantity} for a total of {currency}{total}")