def create_google_doc(service, student_name, folder_id):
    metadata = {
        "name": student_name,
        "mimeType": "application/vnd.google-apps.document",
        "parents": [folder_id]
    }

    doc = service.files().create(
        body=metadata,
        fields="id"
    ).execute()

    return doc["id"]


def insert_text(service, doc_id, message):
    requests = [
        {
            "insertText": {
                "location": {"index": 1},
                "text": message
            }
        }
    ]

    service.documents().batchUpdate(
        documentId=doc_id,
        body={"requests": requests}
    ).execute()