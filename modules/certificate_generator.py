from PIL import Image
from modules.qr_generator import qr_obj
from PIL import ImageDraw, ImageFont
import os

def load_certificate_template(template_path):
    img = Image.open(template_path)
    rgba_img = img.convert("RGBA")
    return rgba_img

def prepare_qr(qr_img, size):
    target_width = size
    target_height = size

    new_img = qr_img.resize((target_width, target_height), Image.NEAREST)
    return new_img

def paste_qr_onto_certificate(cert_img, qr_img, pos):
    x, y = pos
    cert_img.paste(qr_img, pos)
    return cert_img

def add_student_name(cert_img, name, position):
    draw = ImageDraw.Draw(cert_img)

    x, y = position

    # Default font (works everywhere, no setup required)
    font = ImageFont.truetype("arial.ttf", 60)

    draw.text(
    (x, y),
    name,
    fill="black",
    font=font,
    anchor="mm"
)

    return cert_img

def save_certificate(cert_img, student_name):
    safe_name = student_name.replace(" ", "_")

    filename = f"{safe_name}_certificate.png"

    output_folder = "output/certificates"

    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, filename)

    cert_img.save(file_path, "PNG")

    return file_path

def create_certificate(student_name, folder_id):
    url = f"https://drive.google.com/drive/folders/{folder_id}"

    qr_img = qr_obj(url)

    cert = load_certificate_template("C:/Users/E5550/Downloads/New folder/codeChallenges/CodeChallenge/morningStar/templates/Untitled.png")

    width, height = cert.size

    qr_size = 300
    qr_img = prepare_qr(qr_img, qr_size).convert("RGBA")


    qr_position = (
        int(width * 0.435),
        int(height * 0.63)
    )

    name_position = (
    width // 2,
    int(height * 0.54)
    )

    print("CERT SIZE:", cert.size)
    print("QR POSITION:", qr_position)
    print("NAME POSITION:", name_position)
    cert = paste_qr_onto_certificate(cert, qr_img, qr_position)


    cert = add_student_name(cert, student_name, name_position)

    path = save_certificate(cert, student_name)

    return path