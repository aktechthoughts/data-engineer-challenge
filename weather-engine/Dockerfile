FROM python:3.6-slim

RUN mkdir -p /app/tests-results
WORKDIR /app

RUN python -m pip install --upgrade pip

COPY weather /app/weather
COPY tests /app/tests
COPY weather-engine.py /app/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY config.json /app/
COPY pytest.ini /app

RUN ["pytest", "-v", "--junitxml=tests-results/result.xml"]

CMD ["python","weather-engine.py"]

