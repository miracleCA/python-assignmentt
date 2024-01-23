FROM python:3.10.7-alpine3.16

## Create a group and user
RUN addgroup -S teambtrtech && adduser -D btrtech -G teambtrtech
USER btrtech

ENV PATH=/home/btrtech/.local/bin:${PATH}

COPY --chown=btrtech:teambtrtech btrtech-assignment /home/btrtech/btrtech-assignment

WORKDIR /home/btrtech/btrtech-assignment

## Install and test.
RUN pip install ".[test]" && pytest

ENTRYPOINT ["event-process"]
