import csv
import webbrowser


REPORT_FILE = "output/reports/processing_report.csv"


def load_students():

    students = []

    with open(
        REPORT_FILE,
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            students.append(row)

    return students



def search_student(query):

    students = load_students()

    query = query.lower()

    matches = []

    for student in students:

        name = student["Student"].lower()

        if query in name:

            matches.append(student)

    return matches



def display_student(student):

    print("\n==============================")
    print("Student Found")
    print("==============================\n")

    print(
        "Name:",
        student["Student"]
    )

    if "Grade" in student:
        print(
            "Grade:",
            student["Grade"]
        )

    print(
        "Folder ID:",
        student["Folder ID"]
    )

    link = (
        "https://drive.google.com/drive/folders/"
        + student["Folder ID"]
    )

    print(
        "\nFolder Link:"
    )

    print(link)

    print(
        "\nStatus:",
        student["Status"]
    )

    print("==============================\n")

    return link



# -----------------------------
# START
# -----------------------------

search = input(
    "Search student: "
)


results = search_student(search)


if len(results) == 0:

    print(
        "\n❌ No student found."
    )


elif len(results) == 1:

    link = display_student(results[0])

    open_folder = input(
        "Open folder? (y/n): "
    )

    if open_folder.lower() == "y":
        webbrowser.open(link)


else:

    print(
        f"\nFound {len(results)} matches:\n"
    )

    for i, student in enumerate(results):

        print(
            f"{i+1}. {student['Student']}"
        )


    choice = int(
        input(
            "\nSelect student number: "
        )
    )


    link = display_student(
        results[choice-1]
    )


    open_folder = input(
        "Open folder? (y/n): "
    )

    if open_folder.lower() == "y":
        webbrowser.open(link)