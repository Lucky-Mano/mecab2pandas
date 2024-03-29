FROM python:slim

LABEL maintainer "Lucky <phatbowie@gmail.com>"

ENV DIR=/opt

WORKDIR ${DIR}

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install build-essential git make curl xz-utils file swig mecab libmecab-dev mecab-ipadic-utf8 -y \
  && pip install -U --no-cache-dir pip setuptools jupyterlab \
  && git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
  && cd mecab-ipadic-neologd \
  && ./bin/install-mecab-ipadic-neologd -n -u -y \
  && cp /etc/mecabrc /usr/local/etc/mecabrc \
  && apt-get purge build-essential -y

COPY ./mecab2pandas ${DIR}/mecab2pandas
COPY ./setup.py ${DIR}/setup.py

RUN pip install -e .

COPY ./notebooks ${DIR}/notebooks
COPY ./tests ${DIR}/tests

WORKDIR ${DIR}/notebooks

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=9000", "--allow-root"]
