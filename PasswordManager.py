from cryptography.fernet import Fernet
import os

# ---- KEY HANDLING ----
def load_or_create_key():
    if not os.path.exists("secret.key"):   # agar key file nahi hai to banao
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key


# Key load
key = load_or_create_key()
fernet = Fernet(key)


# ---- FUNCTIONS ----
def addPass():
    name = input("Enter Account Name: ")
    psw = input("Enter Password: ")

    # Encrypt password
    enc_psw = fernet.encrypt(psw.encode()).decode()

    with open("password.txt", "a") as f:
        f.write(name + "|" + enc_psw + "\n")
    print("Password saved successfully!")


def viewPass():
    if not os.path.exists("password.txt"):
        print("No password saved yet!")
        return

    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
                user, enc_psw = data.split("|")

                # Decrypt password
                try:
                    dec_psw = fernet.decrypt(enc_psw.encode()).decode()
                except Exception:
                    dec_psw = "ERROR (wrong key?)"

                print(f"User: {user} | Password: {dec_psw}")

def editPass(account_name, new_password):
    lines = []
    with open("password.txt", "r") as f:
        lines = f.readlines()

    with open("password.txt", "w") as f:
        for line in lines:
            user, enc_psw = line.strip().split("|")
            if user == account_name:
                # update password
                new_enc = fernet.encrypt(new_password.encode()).decode()
                f.write(user + "|" + new_enc + "\n")
            else:
                f.write(line)
def deletePass(account_name):
    lines = []
    with open("password.txt", "r") as f:
        lines = f.readlines()

    with open("password.txt", "w") as f:
        for line in lines:
            user, enc_psw = line.strip().split("|")
            if user != account_name:   # only keep others
                f.write(line)

    print(f"{account_name} deleted successfully (if it existed).")               

# ---- MAIN PROGRAM ----
MasterPassword = "Sahil"
MasterPass = input("Enter your master password to access: ")

if MasterPass == MasterPassword:
    while True:
        option = input("\nEnter 'add' to add a password, 'view' to view passwords,'edit' to edit passwords , 'delete' to delete passwords ,'q' to quit: ").lower()
        if option == "q":
            print("Bye...")
            break
        elif option == "add":
            addPass()
        elif option == "view":
            viewPass()
        elif option == "edit":
            accout = input("Enter Account Name:")
            newpass = input("Enter YOur new pass:")
            editPass(accout,newpass) 
        elif option == "delete":
            acc = input("Enter account name to delete: ")
            deletePass(acc)
       
        else:
            print("Invalid Option!")
else:
    print("Wrong master password!")

