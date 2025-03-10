.PHONY=pyodide-build

export PYODIDE_ROOT=$(abspath ..)
include ../Makefile.envs

ifeq ($(strip $(PYODIDE_PACKAGES)),)
else
	ONLY_PACKAGES=--only "$(PYODIDE_PACKAGES)"
endif

all: pyodide-build
	mkdir -p $(HOSTINSTALLDIR) $(WASM_LIBRARY_DIR)
	PYODIDE_ROOT=$(PYODIDE_ROOT) python -m pyodide_build buildall . $(PYODIDE_ROOT)/dist \
	$(ONLY_PACKAGES) --n-jobs $${PYODIDE_JOBS:-4} \
	--log-dir=./build-logs

pyodide-build: ../pyodide-build/pyodide_build/**
	$(HOSTPYTHON) -m pip install -e ../pyodide-build

update-all:
	for pkg in $$(find . -maxdepth 1 ! -name ".*" -type d -exec basename {} \; | tail -n +2); do \
		PYODIDE_ROOT=$(PYODIDE_ROOT) python -m pyodide_build mkpkg "$${pkg}" --update; \
	done

clean:
	rm -rf ./*/build ./*/build.log ./*/dist
	rm -rf ./.artifacts ./.libs
