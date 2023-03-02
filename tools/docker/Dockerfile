FROM ghcr.io/getpatchwork/pyenv:latest

ARG UID=1001
ARG GID=1001
ARG TZ="Asia/Shanghai"
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
COPY patchwork /home/patchwork/patchwork
ENV DJANGO_SETTINGS_MODULE patchwork.settings.production

RUN groupadd --gid=$GID patchwork && \
    useradd --uid=$UID --gid=$GID --create-home patchwork && \
    
RUN rm -f /etc/localtime; ln -s /usr/share/zoneinfo/$TZ /etc/localtime

RUN eval "$(pyenv init -)"

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    tzdata \
    vim-gtk \
    sudo \
    wget \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN usermod -s /bin/bash patchwork && \
#    usermod -g root patchwork && \
    chown -R patchwork /home

RUN pip install wheel tox

# we deliberately leave the requirements files in /opt so we can ping the user
# in entrypoint.sh if they change
RUN pip install -r /home/patchwork/patchwork/requirements-prod.txt

#COPY tools/docker/entrypoint.sh /usr/local/bin/entrypoint.sh
#ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
USER patchwork
WORKDIR /home/patchwork/patchwork
