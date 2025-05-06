FROM python:3.13-alpine

WORKDIR /app

# Setup PDM
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
RUN pip install pdm
ENV PYTHONPATH=/usr/local/lib/python3.13/site-packages/pdm/pep582

# install python deps
COPY pdm.lock pyproject.toml README.md /app/
RUN pdm install --production

# Add python source
COPY main.py /app/
RUN pdm install

COPY dockerStart.sh /app/dockerStart.sh

ENTRYPOINT ["./dockerStart.sh"]
