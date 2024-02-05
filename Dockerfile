FROM python:3.11-buster

WORKDIR /.

ARG requirements=requirements.txt

ADD requirements.txt /requirements.txt


RUN apt-get update \
  && apt-get install -y gcc git python3-dev musl-dev libpq-dev   \
  && python -m pip install --no-cache-dir -r $requirements \
  && apt-get remove -y gcc git \
  && apt-get -y autoremove


ADD /. /.

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
