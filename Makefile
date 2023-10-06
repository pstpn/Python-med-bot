PORT_FORWARD=5432

DB_HOST=127.0.0.1
DB_NAME=meddata
DB_PASS=admin
DB_USER=postgres

LOCAL_DB_DSN="postgres://$(DB_USER):$(DB_PASS)@$(DB_HOST):$(PORT_FORWARD)/$(DB_NAME)"

parse-excel:
	python3 utils/excel_parser.py

migrations-up:
	goose -dir sql/migrations postgres $(LOCAL_DB_DSN) up

migrations-down:
	goose -dir sql/migrations postgres $(LOCAL_DB_DSN) down

.PHONY: parse-excel migrations-up migrations-down