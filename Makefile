.SILENT:

export UV_CACHE_DIR := $(CURDIR)/.cache

RED	=	\e[1;31m
GREEN	=	\e[0;32m
CYAN	=	\e[0;36m
WHITE	=	\e[1;37m

PY	=	python3
UV	=	uv
PDB	=	pudb
PIP	=	pip
EXEC	=	./src/__main__.py
RM	=	rm -rf
VENV	=	.venv

all: $(NAME)
	@make build; \
	make run

help:
	@echo '\n$(CYAN)Usage:$(WHITE)\n'; \
	echo '│ make run	- $(EXEC)'; \
	echo '│	make build	- $(PDB) $(EXEC)'; \
	echo '│	make clean	- $(RM) $(VENV) + $(UV_CACHE_DIR)'; \
	echo '│	make help	- this'; \
	echo '│	make all	- make build && make run'

build:
	@if [ ! -d "$(VENV)" ]; then \
		$(UV) venv $(VENV); \
		$(UV) $(PIP) install -e .; \
		echo '\n$(GREEN)Built $(VENV).$(WHITE)\n'; \
	fi


debug: build
	@$(UV) run $(PDB) $(EXEC)

run: build
	@$(UV) run $(EXEC)

clean:
	@$(RM) .cache; \
	$(RM) $(VENV); \
	echo '\n$(CYAN)Deleted $(VENV) + $(UV_CACHE_DIR).$(WHITE)\n'


.PHONY: all clean debug run build

