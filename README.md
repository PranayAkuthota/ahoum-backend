# Ahoum Backend Assignment

## Overview

A Django REST Framework backend application for event management with role-based access control.

Features include:

* User Registration
* Email OTP Verification
* JWT Authentication
* Role-Based Access Control (SEEKER / FACILITATOR)
* Event CRUD Operations
* Event Enrollment
* Enrollment Cancellation
* My Enrollments
* Search
* Filtering
* Ordering
* Pagination
* Swagger API Documentation

---

## Tech Stack

* Python 3.9
* Django 4.2
* Django REST Framework
* Simple JWT
* Django Filter
* DRF Spectacular

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd ahoum-backend
```

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/api/docs/
```

Schema:

```text
http://127.0.0.1:8000/api/schema/
```

---

## Features

### Authentication

* Signup
* Email Verification
* Login
* JWT Refresh

### Event Management

* Create Event
* List Events
* Event Details
* Update Event
* Delete Event

### Enrollment

* Enroll in Event
* Cancel Enrollment
* View My Enrollments

### Advanced Features

* Search
* Filtering
* Ordering
* Pagination
* Swagger Documentation
