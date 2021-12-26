FROM python:3
COPY requirements.txt .
RUN pip install --user -r requirements.txt

ADD main.py /
CMD ["python", "./main.py"]
