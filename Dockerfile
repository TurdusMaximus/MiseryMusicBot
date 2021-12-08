FROM nikolaik/python-nodejs:python3.9-nodejs17
RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y
COPY . /app
WORKDIR /app
RUN chmod 777 /app
RUN pip install -U pyrogram
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -U -r requirements.txt
CMD ["python3", "main.py"]
