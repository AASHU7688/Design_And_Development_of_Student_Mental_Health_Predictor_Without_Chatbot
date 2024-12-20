# Design_And_Development_of_Student_Mental_Health_Predictor_Without_Chatbot

# Design_and_Development_of_Student_Mental_Health_Predictor
This project aims to address the growing concern of mental health among students by providing a machine learning-based web application that predicts the mental health condition of students based on various parameters. The application is designed to offer insights that can assist students, parents, and professionals in taking proactive steps towards mental wellness.

# Features

Custom Dataset: The dataset was created using a Google Form survey distributed in colleges and schools. It includes a variety of features relevant to mental health.

Machine Learning Model: A logistic regression multiclass classifier is used to predict mental health conditions categorized into different levels.

User-Friendly Interface:
Frontend developed using HTML, CSS, and JavaScript for an interactive and responsive user experience.

Backend built with Django for robust and secure data handling.

SQLite Database: Stores user data efficiently for seamless integration with the web application.

Data Visualization: Key insights from the dataset are presented in a user-friendly manner for better understanding.

# How It Works

Users input their details through an intuitive form on the web application.

The data is processed and passed to the trained logistic regression model for predictions.

The model predicts the user's mental health condition and displays it in an understandable format.

# Technology Stack

Frontend: HTML, CSS, JavaScript

Backend: Django

Database: SQLite

Machine Learning: Logistic Regression (Multiclass Classifier)

# Requirements for the Project

Django Framework:

- Version: 4.x or higher (adjust based on the project).
- Reason: Leverages modern Django features like class-based views and enhanced ORM capabilities.

Python:

- Version: 3.10 or higher.
- Reason: Compatible with modern libraries, type hints, and async support.

# Libraries:

- NumPy: >=1.21.0
  For numerical operations in prediction functions.

- joblib: >=1.2.0
  For loading serialized machine learning models.

# Front-End Libraries:

- HTML/CSS for templates.
- Optional: Bootstrap 5.x for responsive design.

# Database:

- SQLite (default for development) or PostgreSQL for production.

# Deployment Requirements:

- Gunicorn: >=20.0.0
- WhiteNoise: >=5.3.0 (for serving static files in production).

# Steps or Commands to Run the Project

1. Download the zip and extract the contents.
2. Open the extracted folder in VSCode.
3. Open the terminal in VSCode.
4. Navigate to the project directory by executing the command:
   ```bash
   cd mental
   ```
5. Run the following command to start the server:
   ```bash
   python manage.py runserver
   ```

