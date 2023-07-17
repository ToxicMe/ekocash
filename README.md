# Ekocash

# Ekocash Shop Management System

The Ekocash Shop Management System is a simple application designed to manage products, sales, and user accounts for a retail shop. The system has two main roles: **Admin** and **User**, each with specific functionalities.

## Admin Functions:

1. **Add Products**: Admin can add new products to the inventory.
2. **Delete Products**: Admin can remove products from the inventory.
3. **Edit Products**: Admin can modify product details such as name, quantity, buy price, and minimum price.
4. **View Inventory**: Admin can see a list of all available products in the inventory.
5. **View Reports**: Admin can access reports related to sales and other important metrics.
6. **View Sales and Edit Sales**: Admin can view sales records and make necessary edits if required.
7. **View and Edit User Accounts**: Admin can manage user accounts, including modifying user details or permissions.
8. **Send Daily Reports**: Admin can send daily reports to designated recipients.

## User Functions:

1. **View Products List**: Users can see a list of all available products in the inventory.
2. **Search for Products**: Users can search for specific products based on their name or other attributes.
3. **Record Sales**: Users can record sales by specifying the product, quantity, payment method, and sold price.
4. **Send Daily Reports**: Users can send daily sales reports.

## Requirements:

To run the Ekocash Shop Management System, ensure you have the following:

- Python3.9+ installed
- Django 4.2.3 framework installed
- Any additional dependencies mentioned in the requirements.txt.

## Installation and Setup:

1. Clone or download the Ekocash Shop Management System repository from (https://github.com/ToxicMe/ekocash.git).
   `git clone https://github.com/ToxicMe/ekocash.git`
2. Install the required dependencies using:
   `pip install -r requirements.txt`
3. Run migrations to create the required database tables:
   `python manage.py migrate`
4. Create a superuser to access the admin panel:
   `python manage.py createsuperuser`
.  Run the development server:
   `python manage.py runserver`

To run the Ekocash Shop Management System using a batch file, follow these steps:

1. Create a new text file and save it with a `.bat` extension (e.g., `run_ekocash.bat`).
2. Open the batch file with a text editor and add the following commands:

```bash
@echo off

REM Replace "PATH_TO_YOUR_VIRTUAL_ENV" with the location of your virtual environment.
set VIRTUAL_ENV_PATH=PATH_TO_YOUR_VIRTUAL_ENV

REM Activate the virtual environment.
call %VIRTUAL_ENV_PATH%\\Scripts\\activate

REM Replace "PATH_TO_YOUR_DJANGO_PROJECT" with the location of your Django project.
set DJANGO_PROJECT_PATH=PATH_TO_YOUR_DJANGO_PROJECT

REM Navigate to the Django project directory.
cd %DJANGO_PROJECT_PATH%

REM Run the Django development server.
python manage.py runserver

```

1. Save the batch file after adding the correct paths.
2. Before running the batch file, make sure you have set up the virtual environment and installed the necessary dependencies for the Ekocash Shop Management System.
3. Double-click the batch file to execute it. This will activate the virtual environment, navigate to your Django project directory, and start the development server.

Please remember to replace the placeholders `PATH_TO_YOUR_VIRTUAL_ENV` and `PATH_TO_YOUR_DJANGO_PROJECT` with the appropriate paths on your system. 

## Usage:

1. Access the admin panel by navigating to 127.0.0.1:8000/shop/admin and log in using your superuser credentials.
2. Use the admin interface to add products, manage sales, and user accounts.
3. Users can access the application at 127.0.0.1:8000/shop/products to view products, record sales, and send daily reports.

## Note:

This Readme.md file is a basic guide to get you started with the Ekocash Shop Management System. For more detailed instructions or additional features, contact the project maintainer. Happy managing!
