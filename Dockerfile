FROM python:3.12-alpine
WORKDIR /home/myapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5051 
CMD [ "python3","sample_app.py"]