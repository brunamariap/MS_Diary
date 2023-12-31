FROM python:latest

LABEL author="Bruna"

WORKDIR /

RUN pip install --upgrade pip

COPY . /

RUN pip install -r requirements.txt
RUN prisma migrate dev

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]