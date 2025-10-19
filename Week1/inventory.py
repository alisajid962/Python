inventory = {
    "Milk": 150,
    "Bread": 100,
    "Eggs": 200,
    "Tooth Paste": 180,
    "Juice": 250,
    "Banana": 120,
    "Mango": 300
}

cart=[]
while True:
    item= input("Enter the items you want to buy (separated with comma,and done for exit): ").strip()
    if item.lower() =="done":
        break
    item=[i.title() for i in item.split(",")]
    for pr in item:
      if pr in inventory:
         cart.append(pr)
      else:
         print("Item Not Present")
    print("--------Cart List ------------------")
    if cart:
       total = 0
       for items in cart:
          total+=inventory[items]
    print("YOur Cart: ",cart)
    print("Total price: ",total)
