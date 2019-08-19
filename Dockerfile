FROM continuumio/miniconda3
# USER root
# RUN chmod -R 777 /opt/
RUN conda install -y -c pyviz pyviz
# RUN conda install -y xarray holoviews geoviews cartopy hvplot pandas
# RUN chmod -R 777 /opt/
WORKDIR /app
# COPY hvplottest.py /app
COPY main.py /app
COPY data/ /app/data/