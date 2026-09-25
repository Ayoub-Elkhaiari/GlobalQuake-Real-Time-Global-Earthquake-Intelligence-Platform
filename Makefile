up:
	docker compose up -d --build
down:
	docker compose down
logs:
	docker compose logs -f
ps:
	docker compose ps
build:
	docker compose build
restart:
	docker compose restart
db-shell:
	docker compose exec postgres psql -U $$POSTGRES_USER -d $$POSTGRES_DB
kafka-shell:
	docker compose exec kafka bash
test:
	python -m pytest
dbt-run:
	docker compose run --rm airflow bash -c 'cd /opt/airflow/dbt/earthquake_analytics && dbt run --profiles-dir /opt/airflow/dbt'
dbt-test:
	docker compose run --rm airflow bash -c 'cd /opt/airflow/dbt/earthquake_analytics && dbt test --profiles-dir /opt/airflow/dbt'
airflow:
	docker compose logs -f airflow
