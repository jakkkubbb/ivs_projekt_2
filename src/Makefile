PYTHON   := python3
ZIP_NAME := ivs_project.zip

SRCS     := $(wildcard *.py)

.PHONY: all run test clean zip help

# Default target: Run the application
all: run

# Run the GUI application
run:
	$(PYTHON) calc_gui.py $(ARGS)

# Run tests using pytest
test:
	$(PYTHON) -m pytest -v test_calc.py

# Clean build artifacts
clean:
	rm -rf __pycache__
	find . -name "*.pyc" -delete || true

# Create a zip archive of the project
zip:
	zip -r $(ZIP_NAME) ./*

# Display help
help:
	@echo "Available targets:"
	@echo "  test   - Run tests using pytest"
	@echo "  clean  - Clean build artifacts"
	@echo "  zip    - Create a zip archive of the project"
	@echo "  help   - Display this help message"
