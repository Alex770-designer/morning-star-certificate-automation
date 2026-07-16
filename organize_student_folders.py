from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

import csv
import time


SCOPES = [
    "https://www.googleapis.com/auth/drive"
]


# --------------------------------------------------
# Google Drive Authentication
# --------------------------------------------------

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


# --------------------------------------------------
# Load student folders
# --------------------------------------------------

def load_students(report_path):

    students = []

    with open(
        report_path,
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Status"] == "Success":

                students.append(row)

    return students



# --------------------------------------------------
# Create folder if missing
# --------------------------------------------------

def create_folder(service, name, parent_id):

    query = (
        f"'{parent_id}' in parents "
        f"and name='{name}' "
        f"and mimeType='application/vnd.google-apps.folder' "
        f"and trashed=false"
    )

    result = service.files().list(
        q=query,
        fields="files(id,name)"
    ).execute()


    folders = result.get(
        "files",
        []
    )


    if folders:
        return folders[0]["id"]


    folder = service.files().create(
        body={
            "name": name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_id]
        },
        fields="id"
    ).execute()


    return folder["id"]



# --------------------------------------------------
# Get ALL files inside student folder
# (Handles Google Drive pagination)
# --------------------------------------------------

def get_folder_contents(service, folder_id):

    files = []

    page_token = None


    while True:

        result = service.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields=(
                "nextPageToken,"
                "files(id,name,mimeType,parents,shortcutDetails)"
            ),
            pageSize=100,
            pageToken=page_token
        ).execute()


        files.extend(
            result.get("files", [])
        )


        page_token = result.get(
            "nextPageToken"
        )


        if not page_token:
            break


    return files



# --------------------------------------------------
# Get original file behind shortcut
# --------------------------------------------------

def get_shortcut_target(service, shortcut_id):

    shortcut = service.files().get(
        fileId=shortcut_id,
        fields="shortcutDetails"
    ).execute()


    target_id = shortcut["shortcutDetails"]["targetId"]


    target = service.files().get(
        fileId=target_id,
        fields="name,mimeType"
    ).execute()


    return target



# --------------------------------------------------
# Classify shortcut
# --------------------------------------------------

def classify_file(service, item):

    if item["mimeType"] != (
        "application/vnd.google-apps.shortcut"
    ):
        return None


    target = get_shortcut_target(
        service,
        item["id"]
    )


    name = target["name"].lower()
    mime = target["mimeType"]


    print(
        f"Checking: {target['name']}"
    )


    # JPG event photos

    if mime.startswith("image/"):

        if name.endswith(".jpg"):
            return "events"


        elif name.endswith(".jpeg"):
            return "ceremony"



    # Audio files

    elif (
        mime.startswith("audio/")
        or name.endswith(".m4a")
    ):

        return "audio"


    return None



# --------------------------------------------------
# Move shortcut
# --------------------------------------------------

def move_file(
    service,
    file_id,
    old_parent,
    new_parent
):

    service.files().update(
        fileId=file_id,
        addParents=new_parent,
        removeParents=old_parent,
        fields="id,parents"
    ).execute()



# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":


    drive_service = get_drive_service()


    students = load_students(
        "output/reports/processing_report.csv"
    )


    print(
        f"\nStudents found: {len(students)}"
    )


    total_moved = 0



    for index, student in enumerate(
        students,
        start=1
    ):

        student_name = student["Student"]
        folder_id = student["Folder ID"]


        print("\n" + "=" * 60)
        print(
            f"{index}/{len(students)} : {student_name}"
        )


        try:


            events_folder = create_folder(
                drive_service,
                "Morning Star Events",
                folder_id
            )


            audio_folder = create_folder(
                drive_service,
                "Morning Star Audios",
                folder_id
            )


            ceremony_folder = create_folder(
                drive_service,
                "Morning Star Certification Ceremony",
                folder_id
            )


            contents = get_folder_contents(
                drive_service,
                folder_id
            )


            print(
                f"Files found: {len(contents)}"
            )


            for item in contents:


                # Skip folders

                if item["mimeType"] == (
                    "application/vnd.google-apps.folder"
                ):
                    continue



                category = classify_file(
                    drive_service,
                    item
                )



                if category == "events":

                    move_file(
                        drive_service,
                        item["id"],
                        folder_id,
                        events_folder
                    )

                    print(
                        f"📸 Moved event: {item['name']}"
                    )

                    total_moved += 1



                elif category == "audio":

                    move_file(
                        drive_service,
                        item["id"],
                        folder_id,
                        audio_folder
                    )

                    print(
                        f"🎵 Moved audio: {item['name']}"
                    )

                    total_moved += 1



                elif category == "ceremony":

                    move_file(
                        drive_service,
                        item["id"],
                        folder_id,
                        ceremony_folder
                    )

                    print(
                        f"🏅 Moved ceremony: {item['name']}"
                    )

                    total_moved += 1



        except Exception as e:

            print(
                f"❌ Failed {student_name}: {e}"
            )


        time.sleep(1)



    print("\n" + "=" * 60)
    print("ORGANIZATION COMPLETE")
    print("=" * 60)
    print(
        f"Total shortcuts moved: {total_moved}"
    )