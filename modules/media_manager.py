import os

ALLOWED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".mp4", ".mov", ".m4a")


def get_media_files(folder_path):
    files = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        if not os.path.isfile(full_path):
            continue

        if item.lower().endswith(ALLOWED_EXTENSIONS):
            files.append(full_path)
    return files
    