FROM docker:dind

RUN apk update

RUN apk add --no-cache openjdk11-jre fontconfig ttf-dejavu unzip openssl bash openssh git aws-cli

RUN apk add --no-cache jenkins

COPY jenkins-entrypoint.sh /usr/bin/jenkins-entrypoint.sh

ENV DOCKER_HOST=unix:///var/run/docker.sock

ENTRYPOINT /usr/bin/jenkins-entrypoint.sh