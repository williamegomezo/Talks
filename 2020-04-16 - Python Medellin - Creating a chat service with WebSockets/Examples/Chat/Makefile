create-db:
	docker exec chat-postgres bin/bash /db-scripts/create_db.sh

clean-db:
	docker-compose down -v

run-dockers:
	docker-compose up

run:
	cd app && python app.py
	cd ..

revision:
	cd app && alembic revision --autogenerate -m "Revision"
	cd ..

migrate:
	cd app && alembic upgrade head
	cd ..