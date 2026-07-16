import csv
import sqlite3
from datetime import datetime


DATABASE = "morningstar.db"


def import_students():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    with open(
        "output/reports/processing_report.csv",
        newline="",
        encoding="utf-8"
    ) as file:


        reader = csv.DictReader(file)


        for row in reader:


            if row["Status"] == "Success":


                cursor.execute("""
                INSERT OR IGNORE INTO students
                (
                    name,
                    grade,
                    folder_id,
                    status,
                    created_date
                )

                VALUES (?, ?, ?, ?, ?)

                """,
                (

                    row["Student"],

                    row.get("Grade", ""),

                    row["Folder ID"],

                    row["Status"],

                    datetime.now().strftime(
                        "%Y-%m-%d"
                    )

                ))


    conn.commit()

    conn.close()


    print("Students imported!")



if __name__ == "__main__":

    import_students()