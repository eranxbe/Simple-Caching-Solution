FROM python:3.7.13-bullseye

WORKDIR /src

RUN pip install requests

COPY . .

CMD ["python", "-m", "unittest", "Unittests.py"]