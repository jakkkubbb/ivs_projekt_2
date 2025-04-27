PYTHON   := python3


FILES_TO_COPY := ../.git ../plan ../src ../.editorconfig ../.gitignore ../hodnoceni.txt ../LICENSE ../README.md ../screenshot.png ../skutecnost.txt
TEAM_PACK_NAME := xzansim00_xgajdoa00_xmizenj00_xbafalm00



.PHONY: all install run test clean pack ispack doc stddev help

# Default target: Run the application
all: install run


install:
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install pytest || true

# Run the GUI application
run:
	$(PYTHON) calc_gui.py $(ARGS)



# Run tests using pytest
test:
	$(PYTHON) -m pytest -v test_calc.py


# Pack the project
pack: clean doc
	mkdir -p ../../$(TEAM_PACK_NAME)/doc && cp -a ./doc/. ../../$(TEAM_PACK_NAME)/doc
	mkdir -p ../../$(TEAM_PACK_NAME)/install && cp -r ./setup/. ../../$(TEAM_PACK_NAME)/install
	mkdir -p ../../$(TEAM_PACK_NAME)/repo && cp -a ../. ../../$(TEAM_PACK_NAME)/repo
	cd ../.. && zip -qr $(TEAM_PACK_NAME)_wis.zip $(TEAM_PACK_NAME)
	rm -rf ../../$(TEAM_PACK_NAME)


#cp ../dokumentace.pdf ../../$(TEAM_PACK_NAME)
ispack: clean $(WIS_DOC_FILES) $(SRC_FILES) $(TEST_SRC_FILES)
	mkdir -p ../../$(TEAM_PACK_NAME) && cp ../hodnoceni.txt ../../$(TEAM_PACK_NAME)
	mkdir -p ../../$(TEAM_PACK_NAME)/src/ && cp ./*.py ../../$(TEAM_PACK_NAME)/src
	cp ../odevzdani.txt ../../$(TEAM_PACK_NAME)
	cd ../.. && zip -qr $(TEAM_PACK_NAME)_is.zip $(TEAM_PACK_NAME)
	rm -rf ../../$(TEAM_PACK_NAME)


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
	$(PYTHON) stddev.py < ./standard_deviation_data/data1.txt
	$(PYTHON) stddev.py < ./standard_deviation_data/data.txt
	$(PYTHON) stddev.py < ./standard_deviation_data/data2.txt
	
	

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
