FROM python:3.10
WORKDIR /app
COPY /templates /app/templates
COPY app.py /app
COPY Dockerfile /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV NAME webapp
CMD ["python", "app.py"]


