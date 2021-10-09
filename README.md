
create virtualenv
activate virtualenv

install the requirements.txt file:
	pip install -r requirements.txt

Check if rebbitmq-server is running

Start Celery:
	celery -A celeryTask worker -l info -P eventlet

Run runCelery.py to start celery worker:
	python runCelery.py

Run the djnago project(routeTask):
	python manage.py runserver

Postman collection are shared:
	route_task_api.postman_collection.json
