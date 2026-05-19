export UV_CACHE_DIR := $(CURDIR)/.cache

RED	=	\e[1;31m
GREEN	=	\e[0;32m
CYAN	=	\e[0;36m
WHITE	=	\e[1;37m

PY	=	python3
UV	=	uv
PDB	=	pudb
PIP	=	pip3
EXEC	=	./src/__main__.py
RM	=	rm -rf
VENV	=	.venv


all: $(NAME)
	make build

build:
	$(PY) -m venv .env
	$(UV) $(PIP) install -e

debug:
	$(UV) run $(PDB) $(EXEC)

run:
	$(UV) run $(EXEC)

clean:
	@$(RM) .cache; \
	$(RM) $(VENV); \
	echo '\n$(CYAN)Deleted $(VENV) + $(UV_CACHE_DIR).$(WHITE)\n'


.PHONY: all clean debug run build

