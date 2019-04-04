FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /api
WORKDIR /api
COPY requirements.txt /api/
RUN pip install -r requirements.txt
COPY . /api/
EXPOSE 8000
CMD exec gunicorn core.wsgi:application --bind 0.0.0.0:8000