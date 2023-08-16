get-req:
	poetry export --without-hashes --format=requirements.txt > server/requirements.txt
	poetry export --without-hashes --format=requirements.txt > tg-bot/requirements.txt