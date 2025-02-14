FROM python:latest

WORKDIR /frontend

COPY . /frontend 
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install requests
EXPOSE 80


CMD ["python", "app.py"]
