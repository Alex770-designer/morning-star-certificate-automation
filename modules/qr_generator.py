import qrcode
from PIL import Image

def folder_URL (folder_id):
    return f"https://drive.google.com/drive/folders/{folder_id}"

def qr_obj (url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.convert("RGB")
    return img

