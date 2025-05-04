# Healthcare Backend System

This project is a backend system built for a healthcare application using Django, Django REST Framework (DRF), and PostgreSQL. It provides secure user authentication and functionality to manage patient and doctor records, along with the ability to assign doctors to patients.

## Objective

The goal of this assignment is to implement a secure and well-structured backend system that allows users to:

- Register and log in securely using JWT-based authentication.
- Perform CRUD operations on patients and doctors.
- Assign doctors to patients and view those mappings.
- Store all data in a PostgreSQL database using Django's ORM.

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- Environment variable handling using `python-decouple`

## API Overview

### 1. Authentication

- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Log in and receive a JWT token

### 2. Patient Management

- `POST /api/patients/` - Create a new patient (requires authentication)
- `GET /api/patients/` - Retrieve all patients created by the user
- `GET /api/patients/<id>/` - Get details of a specific patient
- `PUT /api/patients/<id>/` - Update a patient’s information
- `DELETE /api/patients/<id>/` - Delete a patient

### 3. Doctor Management

- `POST /api/doctors/` - Create a new doctor (requires authentication)
- `GET /api/doctors/` - Retrieve all doctors
- `GET /api/doctors/<id>/` - Get details of a specific doctor
- `PUT /api/doctors/<id>/` - Update a doctor’s information
- `DELETE /api/doctors/<id>/` - Delete a doctor

### 4. Patient-Doctor Mappings

- `POST /api/mappings/` - Assign a doctor to a patient
- `GET /api/mappings/` - View all mappings
- `GET /api/mappings/<patient_id>/` - View all doctors assigned to a specific patient
- `DELETE /api/mappings/<id>/` - Remove a doctor from a patient

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/assignment.git
   cd assignment
