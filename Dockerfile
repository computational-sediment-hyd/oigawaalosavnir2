FROM continuumio/miniconda3:4.5.12

# RUN conda install -y -c pyviz pyviz
RUN conda install -y -c conda-forge numpy xarray pandas cartopy
RUN conda install -y -c pyviz holoviews
RUN conda install -y -c pyviz geoviews
RUN conda install -y -c pyviz hvplot

WORKDIR /app

COPY main.py /app

COPY data/ /app/data/