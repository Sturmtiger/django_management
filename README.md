# Manual
./manage.py migrate

./manage.py loaddata db.json (use it to load data from app fixtures)

# Celery
celery -A celery_app worker -B -l INFO -Q create_statistics,send_mail *- (run scheduled task `create_statistics` and its subtask `send_mail_if_overtime` in different queues)*
