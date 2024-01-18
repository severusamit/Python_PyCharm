is_goodCredit =True
price =1000000
#down_Payment=0
if is_goodCredit :
    print("You need to put down 10%")
    down_Payment = price * .1
else :
    print("put 20% down payment")
    down_Payment =price * .2
print(f"Down Payment : ${down_Payment}")


