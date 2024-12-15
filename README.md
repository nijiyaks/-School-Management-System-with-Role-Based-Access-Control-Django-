# School-Management-System-Project-Django-
## Overview:- 
The School Management System is a web application developed using Django, designed to streamline administrative, library, and student management tasks in an educational institution. The application is tailored for role-based access, ensuring that users can access and manage specific functionalities based on their roles: Admin, Office Staff, and Librarian.

## Key Features:- 
**Admin Role**
  1)Full access to all features.
  2)Manage (create, edit, delete) accounts for Office Staff and Librarians.
  3)Perform CRUD operations on student records, library histories, and fees records.
**Office Staff Role**
  1)Access to all student details.
  2)Manage (add, edit, delete) fees history.
  3)View library borrowing records and student reviews.
**Librarian Role**
  1)View-only access to student details and library history.
  2)Focused on managing and viewing borrowing records.

Dashboards:-  
**Admin Dashboard**:-
Comprehensive control over the system.
Office Staff Dashboard: Access to manage fees and view records.
Librarian Dashboard: View-only capabilities for library and student records.

**Student Management**:-
CRUD operations on student details (name, division, roll number, etc.).
Enforces unique roll numbers for students within a division.

**Library Management**:-
Track library borrowing history.
Add, edit, delete borrowing records (admin and office staff only).
View borrowing status (borrowed/returned).

## Core Django Libraries:-

Django==5.1.1
djangorestframework==3.15.2
django-filter==24.3
sqlparse==0.5.1
django-allauth==64.2.1
djangorestframework-simplejwt==5.3.1
PyJWT==2.9.0
jwcrypto==1.5.6
phonenumbers==8.13.45

## Technologies used:-

1)Django: Web framework for building the application.

2)Django Rest Framework (DRF): For creating the RESTful API.

3)JWT Authentication: For secure authentication via tokens.

4)phonenumbers: For parsing, formatting, and validating phone numbers.

5)pytz: For managing timezones and timezone-aware datetime objects.

6)Python: Core language used for backend logic.

7)SQLite: Database systems for storing application data.

8)Virtual Environment (venv): Used for isolating project dependencies and creating a clean development environment.

## Installation:-

Make sure you have Python and pip installed on your system.

Python >= 3.8
pip (Python package installer)

## Clone the Repository: 

git clone https://github.com/nijiyaks/School-Management-System-Project-Django-.git      
cd School-Management-System-Project-Django-

