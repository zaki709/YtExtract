.PHONY: init
init:
	docker compose build

.PHONY: up
up:
	docker compose up -d

.PHONY: down
down:
	docker compose down

.PHONY: run
run:
	docker exec -it ytextract python3 src/main.py $(url)

.PHONY: shell
shell:
	docker exec -it ytextract /bin/bash