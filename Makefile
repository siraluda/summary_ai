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

image:
	docker build -t siraluda/summarize_ai:latest .

run-container:
	docker run \
    --name summarize_ai_app \
    --mount source=summarize_ai_vol,target=/code \
    -p 80:80 siraluda/summarize_ai
	
all: install lint test format