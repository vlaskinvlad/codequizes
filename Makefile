DOCKER = docker
PYTHON = python
REPO = docker.locarta.co
NAME = ds-base
IMAGE = ds-base

GIT_VERSION := $(shell git describe --abbrev=7 --dirty --always --tags)

TAG = $(GIT_VERSION)

SERVER_PORT ?= 8888
PWD := $(shell pwd)
WORKDIR ?= "$(PWD)"
SERVER_VERSION ?= "latest"
USER := $(shell whoami)

server:
	$(DOCKER) run -d -p $(SERVER_PORT):8888 \
		-v $(WORKDIR):/home/jovyan \
		--name $(NAME)-$(USER) \
		$(IMAGE) \
		start-notebook.sh \
		--NotebookApp.token=''

stop_server:
		$(DOCKER) rm -f $(NAME)-$(USER)

test:
		pytest .

docker:
		$(DOCKER) build -t $(NAME) .

build:
		 make docker

push:
		$(DOCKER) push $(REPO)/$(NAME):latest
			$(DOCKER) push $(REPO)/$(NAME):$(TAG)

tag:
		$(DOCKER) tag $(NAME) $(REPO)/$(NAME):latest
			$(DOCKER) tag $(NAME) $(REPO)/$(NAME):$(TAG)

run:
		$(DOCKER) run --name $(NAME) -d -p 8080:80 $(NAME)

stop:
		$(DOCKER) rm -f $(NAME)

rm_containers:
		$(DOCKER) ps -aq | xargs $(DOCKER) rm || true

rmi_images:
		$(DOCKER) rmi -f $(NAME) $(REPO)/$(NAME):latest $(REPO)/$(NAME):$(TAG) || true

venv:
		eval $(source venv/bin/activate)
