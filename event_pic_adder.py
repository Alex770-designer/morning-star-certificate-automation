from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from modules.drive_manager import upload_file
import csv
import os

PHOTO_FOLDER = "event_pics"

SCOPES = [
    "https://www.googleapis.com/auth/drive"
]


def get_services():
    flow = InstalledAppFlow.from_client_secrets_file(
        "creds/google_credentials.json",
        SCOPES
    )

    creds = flow.run_local_server(port=0)

    return build("drive", "v3", credentials=creds)


def load_student_folders(csv_path):
    students = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students

def find_student_photo(student_name):
    extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".heic"
    ]

    base_name = student_name.replace(" ", "_")

    for ext in extensions:
        photo_path = os.path.join(
            PHOTO_FOLDER,
            base_name + ext
        )

        if os.path.exists(photo_path):
            return photo_path

    return None

students = load_student_folders(
    "output/reports/processing_report.csv"
)

drive_service = get_services()

uploaded = 0
missing = 0

for student in students:

    student_name = student["Student"]
    folder_id = student["Folder ID"]

    photo_path = find_student_photo(student_name)

    if photo_path:

        upload_file(
            drive_service,
            photo_path,
            folder_id
        )

        print(f"✔ Uploaded {os.path.basename(photo_path)}")
        uploaded += 1

    else:

        print(f"❌ Missing photo for {student_name}")
        missing += 1


print("\n==========================")
print("Upload Complete")
print("==========================")
print(f"Uploaded: {uploaded}")
print(f"Missing : {missing}")