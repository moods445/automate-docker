FROM  ubuntu:20.04
RUN  apt-get update \
     && apt-get install -y python3 python3-venv libaugeas0  \
     && python3 -m venv /opt/certbot/ \
     && /opt/certbot/bin/pip install --upgrade pip \
     && /opt/certbot/bin/pip install certbot \
     && ln -s /opt/certbot/bin/certbot /usr/bin/certbot

