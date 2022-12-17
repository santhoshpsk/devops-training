#!/bin/bash

dockerd-entrypoint.sh &

sleep 10

java -jar /usr/share/webapps/jenkins/jenkins.war