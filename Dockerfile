FROM pypy:3-onbuild

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install -r requirements.txt

ONBUILD COPY . /usr/src/app
EXPOSE 5101:5101
CMD ["gunicorn",  "tss_be:app", "-b :5101"]
