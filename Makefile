.PHONY: install run

install:
	if [ ! -d "venv" ]; then python3 -m venv venv; fi
	. venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && python src/webImobing/main.py