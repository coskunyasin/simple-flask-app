FROM python:3.11-slim-buster
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install graypy
ENTRYPOINT ["python"]
CMD ["app.py"]
