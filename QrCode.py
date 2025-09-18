import qrcode
def GenerateQrCode(text):
    Generateqr = qrcode.make(text)
    Generateqr.show()     

print("Welcome to QrCode Generator")
print("1.Text")
print("2.Links")
print("3.Whatapp")
print("4.Wifi")
print("5.Exit")
while True:
    Input=int(input("Enter option number to choose: "))
    if Input == 5:
        print("Thanks for using")
        break
    if Input == 1:
        text = input("Enter Text you want to convert into Qr: ")
        GenerateQrCode(text)
    elif Input == 2:
        links = input("Enter Link you want to convert into Qr:")
        GenerateQrCode(links)
    elif Input == 3:
        Whatsapp = input("Enter WhatsApp number with country code (e.g., 923001234567): ")
        GenerateQrCode(f"https://wa.me/{Whatsapp}")
    elif Input == 4:
        name = input("Enter WiFi name: ")
        Pass = input("Enter WiFi password: ")
        wifi_format = f"WIFI:T:WPA;S:{name};P:{Pass};;"
        GenerateQrCode(wifi_format)
    else:   
        print("Invalid Option")