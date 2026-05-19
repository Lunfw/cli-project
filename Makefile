RED	=	\e[1;31m
GREEN	=	\e[0;32m
CYAN	=	\e[0;36m
WHITE	=	\e[1;37m

PY	=	python3


all: $(NAME)
	make build


build:
	python3 setup.py build_ext --inplace
