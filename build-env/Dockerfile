FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y python3 python3-pip git wget unzip curl
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip && \
    unzip sonar-scanner-cli-5.0.1.3006-linux.zip -d /opt && \
    mv /opt/sonar-scanner-5.0.1.3006-linux /opt/sonar-scanner && \
    ln -s /opt/sonar-scanner/bin/sonar-scanner /usr/local/bin/sonar-scanner
RUN pip3 install requests --break-system-packages
USER jenkins
RUN jenkins-plugin-cli --plugins configuration-as-code job-dsl workflow-aggregator git sonar script-security
