FROM continuumio/miniconda3

RUN conda install -y -c pyviz pyviz

WORKDIR /app

COPY main2.py /app

COPY data/ /app/data/