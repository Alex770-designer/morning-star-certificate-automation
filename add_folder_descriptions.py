from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
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

    return build(
        "drive",
        "v3",
        credentials=creds
    )


def load_students(csv_path):

    students = []

    with open(
        csv_path,
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Status"] == "Success":
                students.append(row)

    return students


def update_description(service, folder_id, student_name):

    description = f"""
Welcome to {student_name}'s Morning Star Memory Folder!

This folder contains:

📜 Personalized Morning Star Letter
📸 Morning Star Event Memories
🎵 Morning Star Audios
🏆 Certification Ceremony Photos

Thank you for being part of the Morning Star Program.

Created by:
Aahil Hemani
""".strip()


    service.files().update(
        fileId=folder_id,
        body={
            "description": description
        }
    ).execute()



drive_service = get_drive_service()

students = load_students(
    "output/reports/processing_report.csv"
)


print(f"Updating {len(students)} folders...\n")


for student in students:

    try:

        update_description(
            drive_service,
            student["Folder ID"],
            student["Student"]
        )

        print(f"✔ {student['Student']}")

    except Exception as e:

        print(f"❌ Failed: {student['Student']}")
        print(e)


print("\nDone!")