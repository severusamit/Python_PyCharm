weight =int(input("Weight :"))
unit =input("(L)bs or (K)g : ")
if unit =='L' or unit =='l' :
    converted = weight * .45
    print(f"you are {converted} kilos")
