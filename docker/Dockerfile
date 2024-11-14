FROM python:3.10

# システム依存関係のインストール
RUN apt-get update && apt-get install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    python3-distutils \
    wget \
    build-essential \
    fonts-ipafont-gothic \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

# CRF++ (Cabochaで必要)
COPY CRF++-0.58.tar.gz /tmp/CRF++-0.58.tar.gz
RUN cd /tmp/ \
    && tar zxf CRF++-0.58.tar.gz \
    && cd CRF++-0.58 \
    && ./configure \
    && make \
    && make install \
    && ldconfig \
    && cd / \
    && rm -rf /tmp/CRF++-0.58*

# Cabocha のインストール
COPY cabocha-0.69.tar.bz2 /tmp/cabocha-0.69.tar.bz2
RUN cd /tmp \
    && tar -jxf cabocha-0.69.tar.bz2 \
    && cd cabocha-0.69 \
    && ./configure --with-charset=utf-8 \
    && make \
    && make install \
    && ldconfig \
    && rm -rf /tmp/cabocha-0.69*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .