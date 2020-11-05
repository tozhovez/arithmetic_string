FROM python:3.8.1-slim AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential gcc git-core

COPY requirements.txt ./
RUN pip install --user -r requirements.txt

FROM python:3.8.1-slim AS build-image
RUN apt-get update && apt-get install -y --no-install-recommends curl
COPY --from=compile-image /root/.local /root/.local

ARG BUILD_VERSION
ENV VERSION=$BUILD_VERSION
ENV PATH=/root/.local/bin:$PATH

COPY . /app
WORKDIR /app

CMD ["python", "./main.py"]
