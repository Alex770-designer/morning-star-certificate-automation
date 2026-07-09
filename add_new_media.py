from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from modules.drive_manager import (
    upload_shared_media,
    create_shortcut
)

from modules.media_manager import get_media_files

import csv


SCOPES = [
    "https://www.googleapis.com/auth/drive"
]


def get_drive_service():

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

            if row["Status"] == "Success":

                students.append(row)

    return students


drive_service = get_drive_service()

students = load_students(
    "output/reports/processing_report.csv"
)


shared_folder_id = "1otbQd3iMZLLh_YhUDW6L1Ph7wnX5iUC2"


new_media = get_media_files("new_media")


shared_files = upload_shared_media(
    drive_service,
    new_media,
    shared_folder_id
)


print(f"Uploaded {len(shared_files)} new files.\n")


for student in students:

    folder_id = student["Folder ID"]

    for media in shared_files:

        create_shortcut(
            drive_service,
            media["name"],
            media["id"],
            folder_id
        )

    print(f"✔ Updated {student['Student']}")


print("\nDone!")