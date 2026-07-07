from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from modules.drive_manager import upload_file

import csv
import os


PHOTO_FOLDER = "event_pics"

REPORT_FILE = "output/reports/processing_report.csv"


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


def load_students(csv_path):
    students = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students


def get_photos(photo_folder):

    extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".heic"
    )

    photos = []

    for file in os.listdir(photo_folder):

        if file.lower().endswith(extensions):

            photos.append(
                os.path.join(photo_folder, file)
            )

    return sorted(photos)


if __name__ == "__main__":

    students = load_students(REPORT_FILE)

    photos = get_photos(PHOTO_FOLDER)

    drive_service = get_services()

    uploaded = 0
    skipped = 0
    failed = 0


    print(f"Students found: {len(students)}")
    print(f"Photos found: {len(photos)}\n")


    if len(students) != len(photos):
        print("⚠ WARNING:")
        print("Number of students and photos do not match.")
        print("Please verify before continuing.\n")


    for student, photo in zip(students, photos):

        student_name = student["Student"]
        folder_id = student["Folder ID"]


        if student["Status"] != "Success":

            print(
                f"⚠ Skipping {student_name} "
                "(folder creation failed)"
            )

            skipped += 1
            continue


        try:

            upload_file(
                drive_service,
                photo,
                folder_id
            )


            print(
                f"✔ Uploaded {os.path.basename(photo)} "
                f"→ {student_name}"
            )

            uploaded += 1


        except Exception as e:

            print(
                f"❌ Failed uploading "
                f"{student_name}"
            )

            print(
                f"   Error: {e}"
            )

            failed += 1



    print("\n==========================")
    print("Photo Upload Complete")
    print("==========================")
    print(f"Uploaded: {uploaded}")
    print(f"Skipped : {skipped}")
    print(f"Failed  : {failed}")