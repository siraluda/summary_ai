FROM python:3.11.4
WORKDIR /code
COPY . /code/
RUN make install
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80" ]