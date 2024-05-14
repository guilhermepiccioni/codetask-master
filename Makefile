DOCKER = docker
DOCKER-COMPOSE = docker-compose

# Docker Commands

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

# Django Commands
migrate:
	docker-compose run web python manage.py migrate

makemigrations:
	docker-compose run web python manage.py makemigrations

import-data:
	docker-compose run web python manage.py import_data providers.csv courses.csv


# Run all server
run: docker-up migrate makemigrations import-data
	docker-compose logs -f web

.PHONY: clean_local
clean_local:
	$(DOCKER_COMPOSE) down -v --remove-orphans
	$(DOCKER) system prune -af

.PHONY: clean
clean:
	@echo "Cleaning up containers, images, volumes..."
	$(DOCKER) rm -f $(shell $(DOCKER) ps -aq)    	# Remove all containers
	$(DOCKER) rmi -f $(shell $(DOCKER) images -aq)	# Remove all images
	$(DOCKER) volume prune -f						# Remove all volumes
	$(DOCKER) system prune -f						# Cleaner the cache in system
