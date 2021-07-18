FROM python:3

WORKDIR /app

# TODO: add requirements.txt file to install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD "python" "./botFase1.py"
