#inputs
def inputs():
    a = int(input("Enter your digit: ")
    b = input("+,-,*,/,)
    c = int(input("Enter your digit: ")

#function
if b == '+':
    print(a + c)
    return inputs()
elif b == '-':
    print (a - c)
    return inputs()
elif b == '*':
    print (a * c)
    return inputs()
elif b == '/':
    print (a / c)
    print inputs()

