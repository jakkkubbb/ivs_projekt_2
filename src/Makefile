PYTHON   := python3
ZIP_NAME := xzansim00_xgajdoa00_xmizenj00_xbafalm00.zip

SRCS     := $(wildcard *.py)

.PHONY: all run test clean pack doc stddev help

# Default target: Run the application
all: run

# Run the GUI application
run:
	$(PYTHON) calc_gui.py $(ARGS)

# Run tests using pytest
test:
	$(PYTHON) -m pytest -v test_calc.py


# Pack the project for submission
pack: clean doc
	mkdir ../xzansim00_xgajdoa00_xmizenj00_xbafalm00
	cp -r ../.git ../plan ../src ../.editorconfig ../.gitignore ../LICENSE ../README.md ../xzansim00_xgajdoa00_xmizenj00_xbafalm00
	zip -r $(ZIP_NAME) ../xzansim00_xgajdoa00_xmizenj00_xbafalm00
	rm -rf ../xzansim00_xgajdoa00_xmizenj00_xbafalm00
	@echo "Project packed into $(ZIP_NAME)"

# Clean build artifacts
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -name "*.pyc" -delete || true


# Generate documentation using Doxygen
doc:
	doxygen Doxyfile

# Calculate standard deviation from data
stddev:
	$(PYTHON) stddev.py < ./standard_deviation_data/data.txt

# Display help
help:
	@echo "Available targets:"
	@echo "  run     - Run the GUI application"
	@echo "  test    - Run tests using pytest"
	@echo "  clean   - Clean build artifacts"
	@echo "  pack    - Create a zip archive of the project"
	@echo "  doc     - Generate documentation using Doxygen"
	@echo "  stddev  - Calculate standard deviation from data"
	@echo "  help    - Display this help message"
