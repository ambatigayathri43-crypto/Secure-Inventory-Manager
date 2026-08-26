import sys
print("Welcome to Dmart")
print("------------------------")
print("------------------------")
items={
    "rice_bag":{"stock":3,"price":1500},
    "oli_packets":{"stock":4,"price":450},
    "oats_pack":{"stock":7,"price":500},
    }
stock=int(input("Enter total stock:"))
if stock<0:
    print("stop system invalid enter")
    sys.exist()
else:
    print("stock is avaliable")
while True:
 customer_choice=input("enter couster chioce:")
 quantity=int(input("enter how much quantity couster want:"))
 if customer_choice in items:
    avaliable_stock=items[customer_choice]["stock"]
    if avaliable_stock>=quantity:
        print("stock is there")
        total_bill=items[customer_choice]["price"]*quantity
        print("Total bill in RS:",total_bill)
        items[customer_choice]["stock"]-=quantity
    else:
        print("out of stock")
 else:
    print("Sorry out of stock or iteam is not avaliable in Dmart")
