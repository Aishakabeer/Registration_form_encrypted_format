# Student Registration Desktop Application

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)

## Overview

This project is a desktop application for student registration, built using Python and Tkinter. It allows users to register students by entering their details and securely stores the data in an encrypted format. Registered students can be viewed within the application.

## Features

### Student Registration
- Register students with the following details:
  - First Name
  - Last Name
  - Class
  - Phone Number (10 digits, numeric only)
  - Adhar No (12 digits, numeric only)

### Validation
- All fields are mandatory
- Phone number must be exactly 10 digits and numeric
- Adhar number must be exactly 12 digits and numeric

### Secure Data Storage
- Student data is saved in `db.json` in Base64 encoded format
- Data is not human-readable outside the application

### Data Protection
- Protection against casual viewing with third-party tools
- Data remains protected even if file is accessed directly

### View Registered Students
- Display all registered students in a tabular format
- Reads and decodes data from `db.json`

## Usage

### Register a Student
1. Fill in all required fields
2. Click the "Register" button
3. Data is validated and securely stored

### View Registered Students
1. Click the "Display Registered Students" button
2. A new window shows all registered students in a table

## File Structure
.
├── reg_form.py # Main application code

 └── db.json # Encoded student data file


## Security Notes
- Data is encoded using Base64 before saving to `db.json`
- Only the application can properly decode and display the data
- Manual or third-party decoding will not reveal readable student information

## Technologies Used
- **Python 3**
- **Tkinter** - For GUI interface
- **JSON & Base64** - For data serialization and encoding

## How Data Is Stored
1. Student details are validated
2. Data is serialized to JSON
3. JSON string is encoded using Base64
4. Encoded string is appended as a new line to `db.json`

## Data Protection
- Base64 encoding provides basic obfuscation
- `db.json` appears as encoded strings when opened manually
- Protects student information from casual access

## Screenshots
<img width="286" height="261" alt="image" src="https://github.com/user-attachments/assets/80e624c6-9478-46d2-b7c5-b03caa3ff9c5" />

- Registration Form
- Student Display Window

## Requirements
- Python 3.x
- Tkinter (usually comes with Python)

## Installation

python reg_form.py
1. Clone this repository
   ```bash
   git clone Registration_form_encrypted_format
Navigate to the project directory

Run the application

```bash
python reg_form.py
