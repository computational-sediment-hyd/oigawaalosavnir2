FROM continuumio/miniconda3
USER root
RUN conda install -y -c pyviz pyviz
# RUN conda install -y xarray holoviews geoviews cartopy hvplot pandas
WORKDIR /app
COPY rgb_part_ver02.ipynb /app
COPY data/ /app/data/