FROM python:3.7
SHELL ["/bin/bash", "-c"]
WORKDIR /usr/src/app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0:7000"]
EXPOSE 7000

