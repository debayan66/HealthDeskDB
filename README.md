# HealthDeskDB
Hospital Management System (HMS) - Python & MySQL

This is a console-based Hospital Management System implemented in Python with MySQL as the backend database. The system allows hospital staff to manage doctors, patients, admissions, daily charges, and billing in an organized manner. The Tabulate library is used for displaying reports in a tabular format for better readability.

Features
1. Entry Module

Add New Doctors: Insert details of doctors including ID, name, phone number, and specialization.

New Patient Admissions: Automatically generates patient IDs, records patient details, assigns beds (ensuring no conflicts), and links patients to attending doctors.

Daily Charges: Record daily charges for admitted patients.

Bill Collection: Record billing information for discharged patients.

2. Reports Module

Doctor Reports: List all doctors, search by name or specialization.

Patient Reports: Search patients by admission date, name, gender, attending doctor, or diagnosis.

Billing Reports: View detailed treatment charges and expenses for specific patients.

Collection Reports: Track total collections over a specified date range.

Discharge Reports: List patients discharged on a particular date.

3. Tools Module

Delete unwanted admission or daily charges entries for a patient.

4. Exit

Exit the application safely.

Key Functionalities

Database Operations: Uses mysql.connector for executing SQL queries.

Data Validation: Ensures doctor names exist in the database before assigning them to patients and prevents bed conflicts.

User Interaction: Menu-driven interface with input validation for seamless navigation.

Reports: Uses tabulate for visually formatted outputs in the console.

Technologies Used

Python 3.x

MySQL

mysql-connector-python

tabulate library
