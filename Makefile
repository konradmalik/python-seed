ORG=konradmalik
VENV_NAME?=venv
MODULE=example
PACKAGE=demo
PYTHON=${VENV_NAME}/bin/python3

define run_cmd
	${PYTHON} -m ${MODULE}.$(1)
endef

define build_cmd
	docker build \
	--build-arg module=$(1) \
	--build-arg package=$(2) \
	-t $(ORG)/$(1):latest -f Dockerfile.$(1) .
endef

define docker_run_cmd
	docker run --rm \
		$(ORG)/$(1):latest
endef

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements-test.txt requirements-prod.txt
	virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r requirements-test.txt -r requirements-prod.txt
	touch $(VENV_NAME)/bin/activate

run-$(MODULE): venv
	$(call run_cmd,$(PACKAGE))

clean:
	rm -rf ./$(VENV_NAME)
	find . -type f -name "*.pyc" -delete

lint: venv
	${PYTHON} -m autopep8 --in-place -a -a -r ${MODULE}
	${PYTHON} -m autoflake --in-place --recursive --remove-all-unused-imports ${MODULE}
	${PYTHON} -m pylint --exit-zero ${MODULE}
	${PYTHON} -m mypy --ignore-missing-imports ${MODULE}

test: venv
	${PYTHON} -m pytest tests

build-$(MODULE): Dockerfile.$(MODULE)
	$(call build_cmd,$(MODULE),$(PACKAGE))

docker-run-$(MODULE): build-$(MODULE)
	$(call docker_run_cmd,$(MODULE))
