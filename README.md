# Manual
./manage.py migrate

./manage.py loaddata db.json (use it to load data from app fixtures)

# Celery
celery -A celery_app worker -B -l INFO -Q create_statistics,send_mail *- (run scheduled task `create_statistics` and its subtask `send_mail_if_overtime` in different queues)*

# Token-Auth
|URL| Content-Type | Params | Decs |
|--|--|--|--|
|     http://127.0.0.1:8000/api-token-auth/  | application/json | username, password| Get token |
# Interaction with AuthenticatedOnly API URLs
Use your token for this

    curl http://127.0.0.1:8000/api/companies/ -H 'Authorization: Token 4534f7aa7905e012b3c2300408c3dfdf390fcddf'
