# ☁️ Cloud & Local Data Integrity Monitor

## Project Overview

This Python solution was developed during a student position at the **Ludan Group** to ensure data integrity and synchronization between centralized cloud spreadsheets (Google Sheets) and local file system documents.

The core script automates the comparison, filtering, and reporting of documents, identifying any missing or mismatched files between the master document list in Google Sheets and the documents present in the local directory structure.

**Position:** Student Intern, Ludan Group
**Duration:** July 2024 – May 2025

---

## 🚀 Key Features

* **Google Sheets Integration:** Connects to specified Google Sheets documents using the **Google Sheets API** and the `gspread` library.
* **Secure Authentication:** Utilizes **OAuth 2.0** and service account credentials (`credentials.json`) for secure, token-based API access.
* **Automated Data Extraction:** Reads specific data fields (`Document number`, `Binder`, `Revision`) from the cloud master list.
* **File System Scanning:** Recursively scans the local file system structure to catalog all relevant documents.
* **Intelligent File Name Normalization:** Custom Python utilities (`file_name_fix`, `folder_name_fix`) are used to normalize file and folder names to match the naming conventions used in the master document list, ensuring accurate comparison.
* **Difference Reporting:** Generates a report (`missing.txt`) detailing which documents listed in the cloud spreadsheet are **missing** from the local file system.
* **Enhanced Data Monitoring:** Refined data monitoring using custom **JavaScript scripts** (external to this repository's core Python logic).

---

## 🛠️ Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Primary Language** | Python (3.x) | Core logic, data processing, and file system handling. |
| **Cloud API** | Google Sheets API | Programmatic read access to the master document list. |
| **Authentication** | OAuth 2.0 / Service Account | Secure, headless access to Google Cloud resources. |
| **Main Libraries** | `gspread`, `google-auth` | Facilitating the interaction with Google Sheets. |
| **Monitoring** | JavaScript | Custom scripts used for enhanced data monitoring. |

---

## ⚙️ Setup and Installation

Follow these steps to set up the project locally.

### 1. Prerequisites

You must have **Python 3.x** installed on your system.

### 2. Install Dependencies

Install the required Python libraries using `pip`:

```bash
pip install gspread google-auth
```

### 3. Google Sheets API & Authentication

1.  **Enable API:** Enable the **Google Sheets API** for your Google Cloud Project.
2.  **Create Service Account:** Create a Service Account and download the JSON key file.
3.  **Rename File:** Rename the downloaded JSON file to **`credentials.json`** and place it in the root directory of this project.
4.  **Share Sheet:** Share the Google Sheet master document with the email address of the newly created service account.

### 4. Configure `main.py`

Before running, you must update the configuration variables in `main.py`:

1.  **`root_folder`**: Set this to the local path of the parent directory containing all the documents you wish to monitor.
    ```python
    root_folder = "C:\path\to\your\local\documents" # Update this path
    ```
2.  **`sheet_id`**: Update the ID of your Google Sheet Master Document.
    ```python
    sheet_id = "YOUR_GOOGLE_SHEET_ID_HERE" # Update this ID
    ```

---

## ▶️ Usage

To run the data integrity check, execute the main script from your terminal:

```bash
python main.py
```
### Output Files

The script will generate the following text reports in the project directory:

| Filename | Description |
| :--- | :--- |
| **`dict.txt`** | A list of all documents extracted from the Google Sheet Master List. |
| **`all files.txt`**| A list of all files found in the local file system (after initial filtering). |
| **`missing.txt`** | The final report detailing documents found in the Google Sheet but **missing** in the local file system. |