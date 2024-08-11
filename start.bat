@echo Please Wait Process Started

rem Activate the virtual environment
menv\Scripts\activate
echo (activated)

@REM rem Install requirements
pip install -r requirements.txt
echo (installed)

@REM rem Create .env file
echo DB_ENGINE=django.db.backends.postgresql_psycopg2 > .env
echo DB_NAME= __DBName__ >> .env
echo DB_USER= __DB admin __ name >> .env
echo DB_PASSWORD=hAMEED@123 >> .env
echo DB_HOST=___host___ >> .env
echo DB_PORT=5432 >> .env
echo. >> .env
echo DB=development >> .env
echo. >> .env
echo SECRET_KEY="Django Secrate" >> .env
echo. >> .env
echo JWT_SECRET="JWT secrate" >> .env

rem Run Django migrations
python manage.py makemigrations
python manage.py migrate

rem Start the Django development server
python manage.py runserver 8000