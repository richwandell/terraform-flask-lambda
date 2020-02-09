FROM amazonlinux:latest

ENV PATH="/root/.local/bin/:${PATH}"
ENV LANG='en_US.UTF-8'

VOLUME /app_build

RUN yum -y install python3 zip \
    && pip3 install pipenv

COPY build/entrypoint.sh /entrypoint.sh
COPY build/build_archive.sh /build_archive.sh

RUN chmod +x /entrypoint.sh && chmod +x /build_archive.sh
ENTRYPOINT /entrypoint.sh

