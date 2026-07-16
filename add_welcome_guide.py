from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

import csv

SCOPES = [
    "https://www.googleapis.com/auth/drive"
]

# Your Welcome Guide Google Doc / PDF ID
WELCOME_FILE_ID = "1BdXgZhi8Si9AZpPB1H74MdLzL-kkVBu_hzYwIaR_cN0"

# Name that appears inside each student's folder
WELCOME_NAME = "⭐ Start Here"


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


def create_shortcut(
    service,
    target_id,
    shortcut_name,
    folder_id
):

    metadata = {
        "name": shortcut_name,
        "mimeType": "application/vnd.google-apps.shortcut",
        "parents": [folder_id],
        "shortcutDetails": {
            "targetId": target_id
        }
    }

    service.files().create(
        body=metadata
    ).execute()


# ----------------------------------------
# START
# ----------------------------------------

drive_service = get_drive_service()

students = load_students(
    "output/reports/processing_report.csv"
)

print(f"Adding Welcome Guide to {len(students)} folders...\n")

for student in students:

    try:

        create_shortcut(
            drive_service,
            WELCOME_FILE_ID,
            WELCOME_NAME,
            student["Folder ID"]
        )

        print(f"✔ {student['Student']}")

    except Exception as e:

        print(f"❌ {student['Student']}")
        print(e)


print("\n===================================")
print("Finished!")
print("===================================")