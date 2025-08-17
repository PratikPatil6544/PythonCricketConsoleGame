# Virtual environment path
VENV := venv
PYTHON := $(VENV)/bin/python

.DEFAULT_GOAL := help

# -------------------------------------------------------------------
# Setup & Installation
# -------------------------------------------------------------------
venv:				
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	@if [ -f requirements.txt ]; then \
		$(PYTHON) -m pip install -r requirements.txt; \
	else \
		echo "No requirements.txt found. Skipping dependency install."; \
	fi

install: venv		
	@true

# -------------------------------------------------------------------
# Running & Testing
# -------------------------------------------------------------------
run:				
	$(PYTHON) -u -m src.main

test:				
	robot tests/tournament_tests.robot

test-one:			
	@if [ -z "$(NAME)" ]; then \
		echo "Usage: make test-one NAME='Test Case Name'"; \
		exit 1; \
	fi
	robot --test "$(NAME)" tests/tournament_tests.robot

# -------------------------------------------------------------------
# Build Executable
# -------------------------------------------------------------------
build:				
	$(PYTHON) -m pip install pyinstaller
	$(PYTHON) -m PyInstaller --onefile src/main.py
	@echo "Binary available in dist/"

clean:			s
	rm -rf __pycache__ src/__pycache__ tests/__pycache__ dist build *.spec

# -------------------------------------------------------------------
# Help
# -------------------------------------------------------------------
help:				
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'
