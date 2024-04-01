import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4
)

qr.add_data("this is normal qrcode")
qr.make(fit=True)

# Create an image from the QR Code instance
img= qr.make_image(fill_color="blue", back_color="white")

# Save the image to a file
img.save("qrcode.png")

print("QR code image saved as 'qrcode.png'.")
