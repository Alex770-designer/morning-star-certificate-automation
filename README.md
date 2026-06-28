# Morning Star Certificate Automation

## Overview

Morning Star Certificate Automation is a Python application that automates the creation of personalized digital certificates and Google Drive folders for students participating in the Morning Star program.

Instead of manually creating folders, uploading media, writing personalized documents, and generating certificates for every student, this application performs the entire workflow automatically using the Google Drive and Google Docs APIs.

The project was designed to significantly reduce the time required to prepare certificates and media collections for large groups of students while maintaining a personalized experience.

---

## Features

* 📄 Generates a personalized Google Doc for every student.
* 📁 Creates an individual Google Drive folder for each student.
* 🎬 Uploads shared photos, videos, and audio only once to save Google Drive storage.
* 🔗 Automatically creates Google Drive shortcuts to shared media inside each student's folder.
* 🌐 Configures sharing permissions for easy access.
* 📱 Generates a unique QR code that links directly to the student's Google Drive folder.
* 🏅 Places the QR code and student name onto a certificate template.
* 📄 Reads student names directly from a CSV file.
* ⚡ Processes entire classes of students in one batch.
* 📊 Displays a live progress bar with estimated remaining time.
* 📋 Generates a success/failure report after processing.

---

## Motivation

Preparing personalized certificates for large events often involves repetitive manual work:

* Creating folders
* Uploading media
* Writing personalized messages
* Sharing files
* Generating QR codes
* Editing certificates

This project automates the entire workflow, reducing preparation time from hours of repetitive work to a single automated process.

---

## Project Structure

```text
.
├── modules/
│   ├── certificate_generator.py
│   ├── docs_manager.py
│   ├── drive_manager.py
│   ├── media_manager.py
│   ├── message_generator.py
│   └── qr_generator.py
│
├── templates/
│   └── certificate_template.png
│
├── media/
│
├── output/
│   ├── certificates/
│   └── reports/
│
├── creds/
│   └── google_credentials.json
│
├── main.py
├── students.csv
├── requirements.txt
└── README.md
```

---

## Technologies Used

* Python
* Google Drive API
* Google Docs API
* Pillow (PIL)
* qrcode
* CSV
* OAuth 2.0

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/morning-star-certificate-automation.git
cd morning-star-certificate-automation
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Google API Setup

1. Create a Google Cloud project.
2. Enable:

   * Google Drive API
   * Google Docs API
3. Create OAuth Desktop Application credentials.
4. Download the credentials JSON file.
5. Place the file inside:

```text
creds/google_credentials.json
```

---

## Usage

1. Place all shared media files inside the `media/` directory.
2. Place the certificate template inside the `templates/` directory.
3. Create a `students.csv` file with the following format:

```csv
name
John Smith
Jane Doe
Alice Johnson
```

4. Run the program:

```bash
python main.py
```

The application will automatically:

* Create a shared media folder
* Upload media once
* Create a personal Google Drive folder for every student
* Generate a personalized Google Doc
* Create shortcuts to the shared media
* Generate a QR code
* Produce a personalized certificate
* Save certificates locally
* Generate a processing report

---

## Output

After execution, the project generates:

```text
output/
├── certificates/
│   ├── John_Smith_certificate.png
│   ├── Jane_Doe_certificate.png
│   └── ...
│
└── reports/
    └── processing_report.csv
```

Each student's QR code links directly to their personalized Google Drive folder containing:

* Personalized Google Doc
* Shared media shortcuts

---

## Future Improvements

Potential enhancements include:

* Automatic font resizing for long student names
* Parallel uploads for faster processing
* Custom certificate themes
* GUI application
* Automatic printing support
* Resume processing after interruptions
* Duplicate folder detection

---

## License

This project is released under the MIT License.

---

## Acknowledgements

This project was developed to automate certificate generation and media distribution for the Morning Star program using Google's cloud services and Python automation tools.
