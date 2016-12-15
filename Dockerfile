FROM python:3.5-alpine
ADD . .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
CMD ./run
