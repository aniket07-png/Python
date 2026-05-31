import qrcode

url = input("Enter your url: ")

img = qrcode.make(url)

img.save("qrcode.png")
print("qrcode created successfully")
