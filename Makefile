MKFILE_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
SDIST_DIRECTORY := $(realpath $(addprefix $(MKFILE_DIR), sdist))

CREATE_SDIST := python setup.py --quiet sdist

all: clean build_reeco_pkg list_pkgs
.PHONY: all

clean:
	@echo "Removing $(SDIST_DIRECTORY)..."
	@rm -rf $(SDIST_DIRECTORY)

build_reeco_pkg:
	@echo "Building reeco package..."
	@cd $(MKFILE_DIR) && $(CREATE_SDIST) --dist-dir $(SDIST_DIRECTORY)

list_pkgs:
	@echo "Building finished:"
	@find $(SDIST_DIRECTORY) -type f
