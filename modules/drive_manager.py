import os
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

def create_folder(service, student_name):
    metadata = {
        "name": student_name,
        "mimeType": "application/vnd.google-apps.folder"
    }

    folder = service.files().create(
        body=metadata,
        fields="id"
    ).execute()

    return folder["id"]


def create_shared_folder(service, name="MASTER_MEDIA"):
    folder = service.files().create(
        body={
            "name": name,
            "mimeType": "application/vnd.google-apps.folder"
        },
        fields="id"
    ).execute()

    return folder["id"]

def create_shortcut(service, file_name, file_id, student_folder_id):
    try:
        shortcut_metadata = {
            "name": file_name,
            "mimeType": "application/vnd.google-apps.shortcut",
            "parents": [student_folder_id],
            "shortcutDetails": {
                "targetId": file_id
            }
        }

        shortcut = service.files().create(
            body=shortcut_metadata,
            fields="id"
        ).execute()

        return shortcut["id"]

    except Exception as e:
        print(f"Shortcut failed for {file_name}: {e}")
        return None

def upload_file(service, file_path, folder_id):
    file_name = os.path.basename(file_path)

    metadata = {
        "name": file_name,
        "parents": [folder_id]
    }

    media = MediaFileUpload(file_path, resumable=True)

    uploaded = service.files().create(
        body=metadata,
        media_body=media,
        fields="id"
    ).execute()

    return uploaded["id"]


def upload_files(service, file_list, folder_id):
    file_ids = []

    for file_path in file_list:
        file_id = upload_file(service, file_path, folder_id)
        file_ids.append(file_id)

    return file_ids

def make_public(service, file_id):
    permission = {
        "type": "anyone",
        "role": "reader"
    }

    service.permissions().create(
        fileId=file_id,
        body=permission
    ).execute()

def upload_shared_media(service, file_list, shared_folder_id):
    uploaded_files = []

    for file_path in file_list:
        file_id = upload_file(service, file_path, shared_folder_id)

        uploaded_files.append({
            "name": os.path.basename(file_path),
            "id": file_id
        })

    return uploaded_files