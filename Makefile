.PHONY: install run

install:
	@python3 --version | awk '{if ($$2 >= 3.11) print "Python version is acceptable."; else print "Python version must be 3.11 or higher."}'
	@if [ ! -d "venv" ]; then python3 -m venv venv; fi
	. venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && export PYTHONPATH=$(shell pwd) && python src/webImobing/Main.py