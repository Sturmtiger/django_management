# Manual
./manage.py migrate

./manage.py loaddata db.json (use it to load data from app fixtures)

# Celery 
celery -A employee_management_project.celery_app worker -B -l INFO -Q create_statistics,send_mail