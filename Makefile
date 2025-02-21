install:
	pip install -r requirments.txt

format:
	black *.py

lint:
	pylint *.py

run:
	