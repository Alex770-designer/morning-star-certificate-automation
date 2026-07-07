from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from modules.media_manager import get_media_files
from modules.drive_manager import (
    create_folder,
    create_shared_folder,
    upload_shared_media,
    create_shortcut,
    make_public
)
from modules.docs_manager import create_google_doc, insert_text
from modules.message_generator import generate_message
from modules.certificate_generator import create_certificate

import csv
import time
import os


SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents"
]


def get_services():
    flow = InstalledAppFlow.from_client_secrets_file(
        "creds/google_credentials.json",
        SCOPES
    )

    creds = flow.run_local_server(port=0)

    drive_service = build("drive", "v3", credentials=creds)
    docs_service = build("docs", "v1", credentials=creds)

    return drive_service, docs_service


def load_students(csv_path):
    students = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append({
                "name": row["name"],
                "grade": row["grade"]
            })

    return students


def load_completed_students(report_path):
    completed = {}

    if not os.path.exists(report_path):
        return completed

    with open(report_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Status"] == "Success":
                completed[row["Student"]] = row

    return completed


def load_previous_results(report_path):
    results = []

    if not os.path.exists(report_path):
        return results

    with open(report_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            results.append(row)

    return results


if __name__ == "__main__":

    local_folder = "C:/Users/E5550/Downloads/New folder/codeChallenges/CodeChallenge/morningStar/media"
    students_file = "students.csv"

    report_path = "output/reports/processing_report.csv"

    drive_service, docs_service = get_services()

    files = get_media_files(local_folder)
    students = load_students(students_file)

    completed_students = load_completed_students(report_path)

    print(f"\nTOTAL STUDENTS: {len(students)}")


    # ----------------------------
    # Shared media setup
    # ----------------------------
    # Only create shared folder if first run

    if os.path.exists(report_path):

        print("\nExisting report found.")
        print("Skipping shared media recreation.")

        shared_folder_id = None
        shared_files = []


    else:

        shared_folder_id = create_shared_folder(drive_service)

        make_public(
            drive_service,
            shared_folder_id
        )

        shared_files = upload_shared_media(
            drive_service,
            files,
            shared_folder_id
        )

        print(
            f"Shared media uploaded: {len(shared_files)} files"
        )


    # ----------------------------
    # Reporting setup
    # ----------------------------

    results = load_previous_results(report_path)

    start_time = time.time()


    # ----------------------------
    # Main loop
    # ----------------------------

    for i, student in enumerate(students, start=1):

        student_name = student["name"]
        grade = student["grade"]

        total = len(students)


        # ----------------------------
        # Resume mode
        # ----------------------------

        if student_name in completed_students:

            print(
                f"\n⏭ Skipping {student_name} "
                "(already completed)"
            )

            continue


        # ----------------------------
        # Progress bar + ETA
        # ----------------------------

        progress = i / total

        bar_length = 30

        filled = int(progress * bar_length)

        bar = "█" * filled + "-" * (
            bar_length - filled
        )


        elapsed = time.time() - start_time

        processed = i

        avg_time = elapsed / processed

        remaining = avg_time * (
            total - i
        )


        print("\n" + "=" * 60)

        print(
            f"[{bar}] {progress * 100:.1f}%"
        )

        print(
            f"Processing: {student_name}"
        )

        print(
            f"Student {i}/{total}"
        )

        print(
            f"Elapsed: {int(elapsed//60)}m "
            f"{int(elapsed%60)}s"
        )

        print(
            f"ETA: {int(remaining//60)}m "
            f"{int(remaining%60)}s"
        )

        print("=" * 60)


        try:

            folder_id = create_folder(
                drive_service,
                student_name
            )


            make_public(
                drive_service,
                folder_id
            )


            # ----------------------------
            # Shared media shortcuts
            # ----------------------------

            for media in shared_files:

                create_shortcut(
                    drive_service,
                    media["name"],
                    media["id"],
                    folder_id
                )


            message = generate_message(
                student_name,
                grade
            )


            doc_id = create_google_doc(
                drive_service,
                student_name,
                folder_id
            )


            insert_text(
                docs_service,
                doc_id,
                message
            )


            certificate_path = create_certificate(
                student_name,
                folder_id
            )


            print(
                "✔ Done:",
                student_name
            )


            results.append({
                "Student": student_name,
                "Grade": grade,
                "Status": "Success",
                "Folder ID": folder_id,
                "Doc ID": doc_id,
                "Certificate": certificate_path,
                "Error": ""
            })


        except Exception as e:


            print(
                "❌ Failed:",
                student_name
            )

            print(
                "Error:",
                e
            )


            results.append({
                "Student": student_name,
                "Grade": grade,
                "Status": "Failed",
                "Folder ID": "",
                "Doc ID": "",
                "Certificate": "",
                "Error": str(e)
            })


    # ----------------------------
    # Save report
    # ----------------------------

    os.makedirs(
        "output/reports",
        exist_ok=True
    )


    with open(
        report_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:


        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Student",
                "Grade",
                "Status",
                "Folder ID",
                "Doc ID",
                "Certificate",
                "Error"
            ]
        )


        writer.writeheader()

        writer.writerows(results)


    print(
        "\n===== ALL STUDENTS COMPLETE ====="
    )

    print(
        f"Report saved to: {report_path}"
    )