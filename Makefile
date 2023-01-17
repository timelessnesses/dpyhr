POETRY_PYTHON_PATH = $(shell poetry env info --path) # wow copilot ur amazing
POETRY_PYTHON_PATH := $(subst  ,,$(POETRY_PYTHON_PATH)) # remove spaces
ifeq ($(OS),Windows_NT)
	# Windows
	PYTHON = $(addsuffix \Scripts\python.exe,$(POETRY_PYTHON_PATH))
else
	# Linux
	PYTHON = $(addsuffix /bin/python,$(POETRY_PYTHON_PATH))
endif

install_deps:
	pip install poetry
	poetry install

install:
	poetry install

build:
	poetry build

bump:
	poetry version patch
	poetry build

publish:
	poetry publish -u $(PYPI_USERNAME) -p $(PYPI_PASSWORD) --build

test:
	python test_case/main.py