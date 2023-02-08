FROM debian:bullseye

# copy docker-entrypoint and requirements to initialize multi-stage build
COPY ./docker/docker-entrypoint.sh /app/

# implement multi-stage build to leverage build cache (does not re-install packages when code changes)
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-numpy python3-requests

# copy source code
COPY ./src /app/src

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# expose docker container port 80 according to weeve spec
EXPOSE 80
