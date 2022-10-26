FROM Python:3.8.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /HTTP

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./HTTP ./HTTP

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]