import random

def generate_pass():
    upper = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    lower = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    symbol = ("!","@","#","$","%","^","&","*","(",")","_")

    no1 = random.randint(0,50)
    no2 = random.randint(0,30)

    low = (random.sample(lower,2))
    up = (random.sample(upper,2))
    sym = (random.sample(symbol,2))

    password = [str(no1) , str(no2)] + low + sym  + up
    random.shuffle(password)
    password = ''.join(password)
    print(f"Generated Password : {password}")

generate_pass()

while True:
    if input(f"Generate another password (y/n?) :").lower() == "y":
        generate_pass()
    else:
        print("THANKSS!")    



