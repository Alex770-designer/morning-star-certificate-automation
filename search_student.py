import sqlite3
import webbrowser


DATABASE = "morningstar.db"


def search_student(query):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT name, grade, folder_id, status
        FROM students
        WHERE name LIKE ?
        """,
        (f"%{query}%",)
    )


    results = cursor.fetchall()

    conn.close()

    return results



def display_student(student):

    name, grade, folder_id, status = student


    print("\n==============================")
    print("Student Found")
    print("==============================")

    print("Name:", name)
    print("Grade:", grade)

    print("\nFolder ID:")
    print(folder_id)

    link = (
        "https://drive.google.com/drive/folders/"
        + folder_id
    )

    print("\nFolder Link:")
    print(link)

    print("\nStatus:")
    print(status)

    print("==============================\n")

    return link



query = input(
    "Search student: "
)


results = search_student(query)


if len(results) == 0:

    print("\n❌ No student found.")


elif len(results) == 1:

    link = display_student(results[0])


    open_folder = input(
        "Open folder? (y/n): "
    )


    if open_folder.lower() == "y":

        webbrowser.open(link)



else:

    print("\nMultiple matches found:\n")


    for i, student in enumerate(results):

        print(
            f"{i+1}. {student[0]}"
        )


    choice = int(
        input("\nChoose student: ")
    )


    link = display_student(
        results[choice-1]
    )


    open_folder = input(
        "Open folder? (y/n): "
    )


    if open_folder.lower() == "y":

        webbrowser.open(link)