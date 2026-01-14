
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
              "price":1200
        }
  }

  user_is_a_Member = True
  delivery_fee = 0
  total_delivery_fee = 0
  total_amount = 0

  print("Welcome to shoppers please pick your order (just type the number of the item you want)")
  line()
  print(online_store[1])
  line()
  print(online_store[2])
  line()
  print(online_store[3])
  line()


  print("")
  line()
  user_order = int(input("item_number: "))
  line()

  print("")
  line()
  distance = float(input("How far are you? input the distance: "))
  line()

  if 1.0 <= distance <= 3.9:
      delivery_fee += 40

  elif 4.0 <= distance < 8.0:
      delivery_fee += 60

  else: #above 8km
      delivery_fee += 80

  print("")
  line()    
  membership = input("are you a member? type y if yes and n if no: ").upper()
  line()

  if membership != "Y":
        user_is_a_Member = False

  order_amount = online_store[user_order]["price"]

  if order_amount >= 1000:
      
        total_amount = order_amount

        print("")
        print("RESULT")
        line()
        if user_is_a_Member:
              print("Membership discount: Can't be applied to orders above 1000")
        else:
             print("Membership discount: Not a member")

        
        print(f"Delievery fee: {delivery_fee}")
        print(f"Total order amount: {order_amount}")
        print(f"Total delievery fee: {total_delivery_fee}")
        print(f"Total amount to pay: {total_amount}")
        line()

  elif user_is_a_Member:
        
        discount = 0.20 
        total_delivery_fee = delivery_fee - (delivery_fee * discount)
        total_amount = order_amount + total_delivery_fee

        print("")
        print("RESULT")
        line()
        print(f"Total order amount: {order_amount}")
        print(f"Delievery fee: {delivery_fee}")
        print(f"Membership discount: {discount}0")
        print(f"Total delievery fee: {total_delivery_fee}")
        print(f"Total amount to pay: {total_amount}")
        line()

  else:
      
     
      total_delivery_fee = delivery_fee
      total_amount = order_amount + total_delivery_fee
      print("")
      print("RESULT")
      line()
      print(f"Total order amount: {order_amount}")
      print(f"Delievery fee: {delivery_fee}")
      print(f"Membership discount: Not a member")
      print(f"Total delievery fee: {total_delivery_fee}")
      print(f"Total amount to pay: {total_amount}")
      line()








def options():
      run = True
      while run:
            print("")
            print("")
            print("")
            print("1. Scholarship Eligibility Checker")
            print("2. Delivery Fee Calculator")
            print("3. Exit the program")
            pick = int(input("Please pili po kayo: "))
            print("")
            print("")
            if pick == 1:
                  problem1()
            elif pick == 2:
                  problem2()
            else:
                  print("Program terminated")
                  run = False


options()

