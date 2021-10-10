# Route Task


## Installation

- Create virtualenv
- Activate virtualenv

```bash
pip install -r requirements.txt
```

- Check if rabbitmq-server is running.

- Start Celery Worker :
```bash
celery -A celeryTask worker -l info -P eventlet
```

- Run Celery Task :
```bash
python runCelery.py
```

- Run the django project(routeTask) : 
```bash
python manage.py runserver
```

- Postman collection: 
  route_task_api.postman_collection.json

## Steps to Test

- Import the above postman api collection.
- Call api with POST request to add item ({domain}/api/add_item/) with raw json item .
-  Call api with GET request to view item ({domain}/api/view_items/) to check status of item (status of item will change after 10 sec) .

