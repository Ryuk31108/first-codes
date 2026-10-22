a = int(input("\033[33mEnter Your Digit\033[0m: "))
b = (input("\033[33mEnter Your Action +,-,*,/\033[0m: "))
c = int(input("\033[33mEnter Your Digit\033[0m: "))

# main function
if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a / c)
