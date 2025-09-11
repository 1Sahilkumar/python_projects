import random
print("------------StrongPasswordGenerator----------------")
print("1.Generate Password")
print("2.Exit")


uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lowercase = list("abcdefghijklmnopqrstuvwxyz")
digits = list("0123456789")
special = list("!@#$%^&*()-_+=)")
passwordPattern = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',   
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',  
    '0','1','2','3','4','5','6','7','8','9',              
    '!','@','#','$','%','^','&','*','(',')','-','_','=','+' ]
while True:
    opt = int(input("Enter option :"))
    if opt == 1:
        print("1.Password")
        print("2.Pin")
        pass_pin =int(input("Enter Choice: "))
        if pass_pin == 1:
            length = int(input("Length of Password : "))
            must_have = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(special)
            ]
            remaining = length - 4
            extra = random.choices(passwordPattern, k=remaining)
            password_list = must_have + extra
            random.shuffle(password_list)
            password = "".join(password_list)
            print("Your Password:", "".join(password))
        elif pass_pin == 2:
            length = int(input("Length of Password : "))
            pin = random.choices(digits,k=length)
            password = "".join(pin)
            print("Your Password:", "".join(password))
        else:
            print("Invalid Option")    
    elif opt == 2:
        break
    else:
        print("Invalid Option")    