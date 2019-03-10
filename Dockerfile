FROM ubuntu:18.04

LABEL maintainer="Media Suite <developers@mediasuite.co.nz>"

# These are needed for installing pipenv without errors.
ENV LC_ALL "C.UTF-8"
ENV LANG "C.UTF-8"

# This will tell Pipenv to create the virtual env in the same directory as the project.
ENV PIPENV_VENV_IN_PROJECT 1

WORKDIR /src

RUN \
  apt-get update && \
  apt-get install -y \
    python3 \
    python3-pip \
    nginx \
    supervisor \
    uwsgi \
    uwsgi-plugin-python3 \
    && \
  rm -rf /var/lib/apt/lists

RUN pip3 install pipenv

# Configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY docker-config/nginx-app.conf /etc/nginx/sites-available/default
COPY docker-config/supervisor-app.conf /etc/supervisor/conf.d/
COPY docker-config/uwsgi.ini /src/

# fetches and downloads the project's dependencies
COPY Pipfile /src/Pipfile
COPY Pipfile.lock /src/Pipfile.lock
RUN pipenv install

# Add Server code
COPY server/ /src/server/

# Add Client code
COPY client/dist/ /src/client/dist/

# Django will cry if it doesn't have its precious secret key
RUN SECRET_KEY='x' pipenv run /src/server/manage.py collectstatic --no-input

EXPOSE 80

# adding the start script to the source environment
COPY docker-config/start.sh /src/

# add executable permissions to the script
RUN chmod +x /src/start.sh

CMD ["/src/start.sh"]
