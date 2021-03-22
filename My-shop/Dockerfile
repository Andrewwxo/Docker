FROM python:3.8-buster

WORKDIR /var/app

COPY my-shop/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY my-shop .

EXPOSE 5000   #hint to forward the port


CMD python app.py