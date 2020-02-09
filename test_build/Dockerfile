FROM amazonlinux:latest

ENV PATH="/root/.local/bin/:${PATH}"
ENV LANG='en_US.UTF-8'
VOLUME /app_build

RUN yum -y install python3 unzip

COPY test_build/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh