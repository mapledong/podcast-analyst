.PHONY: install fetch extract publish run validate-all

VENV = .venv/bin
PY = $(VENV)/python

install:
	python3 -m venv .venv
	$(VENV)/pip install -r requirements.txt

fetch:
	$(PY) src/pipeline.py fetch -e $(EP)

extract:
	$(PY) src/pipeline.py extract -e $(EP)

approve:
	$(PY) src/pipeline.py approve -e $(EP) --notes "$(NOTES)"

publish:
	$(PY) src/pipeline.py publish -e $(EP)

run:
	$(PY) src/pipeline.py run -e $(EP)

validate-all:
	$(PY) src/pipeline.py validate --json data/approved/ep477.json
	$(PY) src/pipeline.py validate --json data/approved/ep476.json
	$(PY) src/pipeline.py validate --json data/approved/ep475.json

publish-all:
	$(PY) src/pipeline.py publish -e ep477
	$(PY) src/pipeline.py publish -e ep476
	$(PY) src/pipeline.py publish -e ep475
