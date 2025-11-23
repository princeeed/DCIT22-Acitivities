
def line():
      print("=========================================================================")

#Scholarship Eligibility Checker
def problem1():
      print("below 1.75 or higher")
      print("2.00 and above")
      user_gwa = float(input("Whats your GWA? "))


      if user_gwa <= 1.75:
            annual_income = int(input("Okay great whats your family anuual income? "))

            if annual_income < 150000: #150,000
                  print("Full scholarship granted!")

            else:
                  print("Partial Scholarship Only")

      elif user_gwa > 1.75 and user_gwa <= 2.0:
            print("Partial Scholarship Only")


      else:
            print("Not eligible")

#Delivery Fee Calculator
def problem2():
  online_store = {
        1:{
              "item_number":1, "item_name":"Make-up Set",
              "price":200
        },
        2:{
              "item_number":2, "item_name":"Milo Energy drink",
              "price":500
        },
        3:{
              "item_number":3, "item_name":"RTX 4090",
              "price":1000
        }
  }

  address = {
        1:{
            "Number": 1, "Address":"Molino IV", "distance":"3km", "fee":40},
        2:{
            "Number": 2, "Address":"Panpaan3",  "distance":"7km",
              "fee":60
        },
        3:{
            "Number": 3,"Address":"Dasma Cavite", "distance":"8km",
            "fee":80
        }
  }


  user_is_a_Member = True


  print("Welcome to shoppers please pick your order (just type the number of the item you want)")
  line()
  print(online_store[1])
  line()
  print(online_store[2])
  line()
  print(online_store[3])



  user_order = int(input("item_number: "))
  print("")
  print("")
  print("")
  line()
  print(address[1])
  line()
  print(address[2])
  line()
  print(address[3])
  line()

  user_address = int(input("Whats your address? "))
  membership = input("are you a member? y/n? ").upper()

  if membership != "Y":
        user_is_a_Member = False

  delievery_fee = address[user_address]["fee"]
  total_order_amount = online_store[user_order]["price"]

  if total_order_amount >= 1000:
        total_delievery_fee = delievery_fee - delievery_fee
        total_amount = total_order_amount + total_delievery_fee

        print("")
        print("")
        line()
        if user_is_a_Member:
              print("Membership discount: Can't be applied")

        print(f"Delievery fee: {delievery_fee}")
        print(f"Total delievery fee: {total_delievery_fee}")
        print(f"Total order amount: {total_order_amount}")
        print(f"Total amount to pay: {total_order_amount}")
        line()
  elif user_is_a_Member:
        discount = 0.20 
        total_delievery_fee = delievery_fee - (delievery_fee * discount)
        total_amount = total_order_amount + total_delievery_fee

        print("")
        print("")
        line()
        print(f"Membership discount: {discount}0")
        print(f"Delievery fee: {delievery_fee}")
        print(f"Total order amount: {total_order_amount}")
        print(f"Total delievery fee: {total_delievery_fee}")
        print(f"Total amount to pay: {total_amount}")
        line()

  else:
      total_amount = total_order_amount + delievery_fee
      print("")
      print("")
      line()
      print(f"Membership discount: Not a member")
      print(f"Delievery fee: {delievery_fee}")
      print(f"Total order amount: {total_order_amount}")
      print(f"Total delievery fee: {delievery_fee}")
      print(f"Total amount to pay: {total_amount}")
      line()



def options():
      print("1. Scholarship Eligibility Checker")
      print("2. Delivery Fee Calculator")
      pick = int(input("Please pili po kayo: "))
      print("")
      print("")
      if pick == 1:
            problem1()
      else:
            problem2()

options()


#Scholarship Eligibility Checker Outputs
#Partial only if mataas ang income

"""
Welcome to shoppers please pick your order (just type the number of the item you want)
=========================================================================
{'item_number': 1, 'item_name': 'Make-up Set', 'price': 200}
=========================================================================
{'item_number': 2, 'item_name': 'Milo Energy drink', 'price': 500}
=========================================================================
{'item_number': 3, 'item_name': 'RTX 4090', 'price': 1000}
item_number:


=========================================================================
{'Number': 1, 'Address': 'Molino IV', 'distance': '3km', 'fee': 40}
=========================================================================
{'Number': 2, 'Address': 'Panpaan3', 'distance': '7km', 'fee': 60}
=========================================================================
{'Number': 3, 'Address': 'Dasma Cavite', 'distance': '8km', 'fee': 80}
=========================================================================
Whats your address? 2
are you a member? y/n? y


=========================================================================
Membership discount: Can't be applied
Delievery fee: 60
Total delievery fee: 0
Total order amount: 1000
Total amount to pay: 1000
=========================================================================


""" 