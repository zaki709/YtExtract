.PHONY: init
init:
	docker compose build

.PHONY: up
up:
	docker compose up -d

.PHONY: down
down:
	docker compose down

.PHONY: shell
shell:
	docker exec -it ytextract /bin/bash