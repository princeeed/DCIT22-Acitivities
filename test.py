def line():
    print("=========================================================================")


# Delivery Fee Calculator
def problem2():
    online_store = {
        1: {"item_number": 1, "item_name": "Make-up Set", "price": 200},
        2: {"item_number": 2, "item_name": "Milo Energy drink", "price": 500},
        3: {"item_number": 3, "item_name": "RTX 4090", "price": 1000}
    }

    print("Welcome to shoppers please pick your order (just type the number of the item you want)")
    line()
    print(online_store[1])
    line()
    print(online_store[2])
    line()
    print(online_store[3])

    user_is_a_Member = True
    delivery_fee = 0

    user_order = int(input("item_number: "))
    membership = input("are you a member? y/n? ").upper()

    if membership != "Y":
        user_is_a_Member = False

    user_distance = float(input("num: "))

    if 1.0 <= user_distance <= 3.9: 
        delivery_fee += 40
    elif 4.0 <= user_distance < 8.0:
        delivery_fee += 60
    else:  # 8 and above
        delivery_fee += 80

    total_order_amount = online_store[user_order]["price"]


    if total_order_amount >= 1000:
        total_delievery_fee = delivery_fee - delivery_fee
        total_amount = total_order_amount + total_delievery_fee

        print("")
        print("")
        line()
        if user_is_a_Member:
            print("Membership discount: Can't be applied")

        print(f"Delievery fee: {delivery_fee}")
        print(f"Total delievery fee: {total_delievery_fee}")
        print(f"Total order amount: {total_order_amount}")
        print(f"Total amount to pay: {total_order_amount}")
        line()

    elif user_is_a_Member:
        discount = 0.20 
        total_delievery_fee = delivery_fee - (delivery_fee * discount)
        total_amount = total_order_amount + total_delievery_fee

        print("")
        print("")
        line()
        print(f"Membership discount: {discount}0")
        print(f"Delievery fee: {delivery_fee}")
        print(f"Total order amount: {total_order_amount}")
        print(f"Total delievery fee: {total_delievery_fee}")
        print(f"Total amount to pay: {total_amount}")
        line()

    else:
        total_amount = total_order_amount + delivery_fee
        print("")
        print("")
        line()
        print(f"Membership discount: Not a member")
        print(f"Delievery fee: {delivery_fee}")
        print(f"Total order amount: {total_order_amount}")
        print(f"Total delievery fee: {delivery_fee}")
        print(f"Total amount to pay: {total_amount}")
        line()


