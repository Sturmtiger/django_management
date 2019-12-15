# Manual
./manage.py migrate

./manage.py loaddata db.json (use it to load data from app fixtures)

# Users
| Username | Password | Description |
|--|--|--|
| simple_user | 123 | No perms (Able to only see the list of companies) |
| reviewer | 123 | Member of 'Reviewers' group(Able to see company details as well) |
| adm | adm | superuser |
