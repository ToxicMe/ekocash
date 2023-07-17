@echo off

rem Activate your virtual environment (if applicable)
call C:\"PATH"\EkoCash\env\Scripts\activate

rem Change to your Django project directory
cd C:\"PATH"\Desktop\EkoCash

rem Start the Django development server
start cmd /k "python manage.py runserver"

rem Wait for the server to start
timeout 5

rem Open the specified URL in the default browser
start "" "http://localhost:8000/shop/products"

rem Exit the batch file
exit
