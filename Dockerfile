FROM continuumio/miniconda3

# RUN conda install -y -c pyviz pyviz
RUN conda install -y -c conda-forge numpy xarray pandas cartopy
RUN conda install -y -c pyviz holoviews
RUN conda install -y -c pyviz geoviews
RUN conda install -y -c pyviz hvplot

WORKDIR /app

COPY main2.py /app

COPY data/ /app/data/