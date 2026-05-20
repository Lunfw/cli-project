export UV_CACHE_DIR := $(CURDIR)/.cache

RED	=	\e[1;31m
GREEN	=	\e[0;32m
CYAN	=	\e[0;36m
WHITE	=	\e[1;37m

PY	=	python3
UV	=	uv
PDB	=	pudb
PIP	=	pip
RM	=	rm -rf
VENV	=	.venv

ARGS	=	$(filter-out $@, $(MAKECMDGOALS))

all: build
	@clear; \
	$(UV) run --no-sync $(PY) -m src

help:
	@echo '\n$(CYAN)Usage:$(WHITE)\n'; \
	echo '│	make run	- $(UV) run --no-sync $(PY) -m src'; \
	echo '│	make build	- $(UV) run --no-sync $(PDB) -m src'; \
	echo '│	make clean	- $(RM) $(VENV) + $(UV_CACHE_DIR)'; \
	echo '│	make help	- this'

build:
	@if [ ! -d "$(VENV)" ]; then \
		$(UV) run $(PY) -m venv $(VENV); \
		$(UV) $(PIP) install -e .; \
		echo '\n$(GREEN)Built $(VENV).$(WHITE)\n'; \
	fi


debug: build
	@$(UV) run --no-sync $(PDB) -m src

run: build
	@$(UV) run --no-sync $(PY) -m src $(ARGS)

clean:
	@$(RM) .cache; \
	$(RM) $(VENV); \
	find . -name "*.pyc" -exec $(RM) {} +; \
	find . -name "*.pyo" -exec $(RM) {} +; \
	find . -name "__pycache__" -exec $(RM) -r {} +; \
	echo '\n$(CYAN)Deleted $(VENV) + $(UV_CACHE_DIR).$(WHITE)\n'


.PHONY: all clean debug run build

