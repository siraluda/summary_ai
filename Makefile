install:
	pip install --no-cache-dir --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=app/ test_app/test_app.py

format:
	black app/*.py

lint:
	pylint --disable=R,C app/main.py

run-server:
	uvicorn app.main:app --reload

update-requirements:
	pip freeze > requirements.txt

all: install lint test format