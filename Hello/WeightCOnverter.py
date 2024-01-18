weight =int(input("Weight :"))
unit =input("(L)bs or (K)g : ")
if unit =='L' or unit =='l' :
    # or unit.upper() =="L"
    converted = weight * .45
    print(f"you are {converted} kilos")
else :
    converted = weight /.45
    print("You are "+str(converted) + "pounds")
