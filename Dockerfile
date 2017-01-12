FROM ubuntu:14.04
MAINTAINER Wrongerror, appledevspecial@163.com

ENV MYSQL_USER=mysql \
    MYSQL_DATA_DIR=/var/lib/mysql \
    MYSQL_RUN_DIR=/run/mysqld \
    MYSQL_LOG_DIR=/var/log/mysql \
    WORK_DIR=/var/www/hawkapi

COPY sources.list /etc/apt/sources.list

RUN echo "deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu trusty main" > /etc/apt/sources.list.d/deadsnakes.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DB82666C

RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu lucid main" > /etc/apt/sources.list.d/nginx-stable-lucid.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    mercurial \
    pkg-config \
    python3.4 \
    python-dev \
    python3.4-dev \
    openssh-server \
    python-pip \
    python3-pip \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server \
    libmysqlclient-dev \
    nginx \
    && apt-get autoremove \
    && apt-get clean \
    && rm -rf ${MYSQL_DATA_DIR} \
    && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

WORKDIR ${WORK_DIR}

COPY hawk_api.conf /etc/nginx/conf.d
RUN mkdir /etc/nginx/logs/

COPY hawkapi /var/www/hawkapi
COPY run /var/www/hawkapi

COPY pip.conf /etc/pip.conf
RUN pip install supervisor
COPY supervisord.conf /etc/supervisord.conf

RUN pip3 install virtualenv
RUN virtualenv -p python3 venv
RUN . venv/bin/activate; \
    pip3 install -r requirements.txt

EXPOSE 3306/tcp 80 3002 8000

VOLUME ["${MYSQL_DATA_DIR}", "${MYSQL_RUN_DIR}"]

ENTRYPOINT ["/sbin/entrypoint.sh"]

CMD ["/usr/bin/mysqld_safe"]