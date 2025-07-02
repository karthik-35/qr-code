import qrcode

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#FFFFFF", back_color="black")
    img.save(file_name)

# Input text to generate QR code for
text = "https://www.youtube.com/"
# File name to save the QR code image
file_name = "qr_code.png"
# Generate the QR code
generate_qr_code(text, file_name)
print(f"QR code saved as {file_name}")
