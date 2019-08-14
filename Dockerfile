FROM continuumio/miniconda3
# USER root
# RUN chmod -R 777 /opt/
RUN conda install -y -c pyviz pyviz
# RUN conda install -y xarray holoviews geoviews cartopy hvplot pandas
# RUN chmod -R 777 /opt/
WORKDIR /app
COPY rgb_part_ver02.ipynb /app
COPY data/ /app/data/