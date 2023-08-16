run:
	./manage.py runserver 0.0.0.0:8000
migrate:
	./manage.py makemigrations
	./manage.py migrate
get-req:
	poetry export --without-hashes --format=requirements.txt > requirements.txt