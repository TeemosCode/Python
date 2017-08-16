import qrcode
from PIL import Image as pimg
qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=4)
qr.add_data("https://github.com/TeemosCode")
qr.make(fit=True)

img = qr.make_image()

img.save("GitHub QrCode")

#linkedIn

qr = qrcode.QRCode(version = 1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=4)
qr.add_data("https://www.linkedin.com/in/ping-che-ho-a10631120/")

im = qr.make_image()
im.save("LinkedInQrCode")


qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=4)
qr.add_data("https://illinois.joinhandshake.com/users/5607153")

handshake = qr.make_image()
handshake.save("HandShake")

