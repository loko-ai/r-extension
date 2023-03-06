FROM r-base
RUN apt-get update && apt-get install python3 python3-pip python3-dev python3.11-venv -y
EXPOSE 8080
RUN python3 -m venv /opt/venv
ADD ./requirements.txt /
RUN  /opt/venv/bin/pip install -r /requirements.txt
ADD ./r_requirements.txt /
ADD ./r_cran_install.sh /
RUN sh "/r_cran_install.sh"
# RUN mkdir -p /opt/software/setup/R
# ADD install_packages.R /opt/software/setup/R/
# RUN Rscript /opt/software/setup/R/install_packages.R
ARG GATEWAY
ENV GATEWAY=$GATEWAY
ADD . /plugin
ENV PYTHONPATH=$PYTHONPATH:/plugin
WORKDIR /plugin/services
CMD  /opt/venv/bin/python3 services.py