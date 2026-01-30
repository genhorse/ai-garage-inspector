FROM sonarqube:lts-community
USER root
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
USER sonarqube
