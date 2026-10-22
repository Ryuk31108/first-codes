import random

small_letter = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
capital_letter = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
numbers = "0","1","2","3","4","5","6","7","8","9"
symbols = "!","@","#","$","%","^","&","*","(",")","-","+","=","{","}","[","]",":",";","'","<",">",",",".","?","/"

def password_generator():
    capitals = random.choices(capital_letter, k=3)
    smalls = random.choices(small_letter, k=3)
    nums = random.choices(numbers, k=3)
    symbs = random.choices(symbols, k=3)
    password = capitals + smalls + nums + symbs
    random.shuffle(password)
    return "".join(password)

password = password_generator()
print(password)
