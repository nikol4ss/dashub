@echo off
call .venv\Scripts\activate
cd api
python manage.py runserver
pause
