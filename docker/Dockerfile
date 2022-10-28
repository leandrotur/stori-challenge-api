FROM python:3.9-slim AS build-stage

WORKDIR /venv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        git && \
    apt-get autoremove -y && \
    apt-get clean && \
    python -m venv /venv

ENV PATH=/venv/bin:$PATH

ADD app/requirements.txt .
RUN pip install --upgrade pip \
    pip install -r requirements.txt

FROM python:3.9-slim AS runtime-stage

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        curl \
        jq \
        less \
        postgresql-client \
        uuid-runtime \
        wget && \
    wget https://github.com/krallin/tini/releases/download/v0.19.0/tini -O \
        /tini && \
    chmod +x /tini && \
    apt-get autoremove -y && \
    apt-get clean

COPY --from=build-stage /venv /venv

ENV PATH=/venv/bin:$PATH \
    PYTHONPATH=/ \
    PYTHONUNBUFFERED=1 \
    PY_ENV=orange \
    PORT=3000 

ADD docker/entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/tini", "/entrypoint.sh"]

HEALTHCHECK --interval=5m --timeout=10s CMD curl -f http://localhost:${PORT}/?healthcheck

WORKDIR /app
COPY app /app
CMD ["app", "start"]

EXPOSE ${PORT}
