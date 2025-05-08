# 📝 TO-DO-LIST Django Project

This is a simple **To-Do List** application built using **Django** and **SQLite** as the database. It allows users to create, edit, and delete tasks, and provides authentication features such as login and signup.

---

## 📁 Project Structure

| File/Folder               | Description                                         |
|---------------------------|-----------------------------------------------------|
| `manage.py`                | Django's command-line utility for project management |
| `db.sqlite3`               | SQLite database for storing user data and tasks    |
| `todo/`                    | Main Django app for managing to-do list functionality |
| `todo/templates/`          | HTML templates for rendering the frontend views   |
| `todo/migrations/`         | Django database migrations                        |
| `todo/__init__.py`         | Python file that marks the `todo` directory as a Python package |
| `todo/admin.py`            | Django admin configuration for the `todo` app     |
| `todo/asgi.py`             | ASGI configuration for asynchronous server support |
| `todo/models.py`           | Defines the data models (To-Do items, User)        |
| `todo/settings.py`         | Django project settings (database, static files, etc.) |
| `todo/urls.py`             | URL routing for the `todo` app                    |
| `todo/views.py`            | Views and logic for handling to-do operations      |
| `todo/wsgi.py`             | WSGI configuration for deploying the app          |

---

## 🖥️ How to Use

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- Django

### 1. Clone the Repository:

```bash
git clone https://github.com/saugatpoudel100/TO-DO-LIST.git
cd TO-DO-LIST
```

### 2. Install Dependencies:

You can install required dependencies using pip:

```bash
pip install -r requirements.txt
```

> Note: If the `requirements.txt` file doesn't exist yet, you can simply install Django:

```bash
pip install django
```

### 3. Apply Database Migrations:

Run the following command to set up the database:

```bash
python manage.py migrate
```

### 4. Create a Superuser (Optional for Admin Access):

If you want to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up an admin username and password.

### 5. Run the Development Server:

Start the Django development server:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.

---

## 📄 Features

- **Task Management**: Users can add, edit, and delete tasks.
- **Authentication**: Users can sign up, log in, and manage their tasks securely.
- **SQLite Database**: Stores tasks and user data.

---

## 🛠️ Technologies Used

- **Django** – Python-based web framework
- **SQLite** – Lightweight database
- **HTML/CSS** – For frontend design

---

## 🙋‍♂️ Author

Developed by **[Saugat Poudel](https://github.com/saugatpoudel100)**  
📧 Contact: *sauggupoudel10@gmail.com*

---


