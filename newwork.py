import qrcode

# Your Google Form URL
url = "https://forms.gle/NnaW3WzRhLeT2F3eA"

# Create QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of border
)

qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("google_form_qr.png")

print("QR code generated and saved as google_form_qr.png")
