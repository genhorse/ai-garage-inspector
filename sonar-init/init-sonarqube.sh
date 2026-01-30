#!/usr/bin/env bash
/opt/sonarqube/docker/entrypoint.sh &
until curl -s "http://localhost:9000/api/system/status" | grep -q '"status":"UP"'; do
    sleep 10
done
curl -s -u admin:admin -X POST "http://localhost:9000/api/users/change_password?login=admin&previousPassword=admin&password=admin123" || true
TOKEN_JSON=$(curl -s -u admin:admin123 -X POST "http://localhost:9000/api/user_tokens/generate?name=ci-token-$(date +%s)")
TOKEN=$(echo "$TOKEN_JSON" | sed -n 's/.*"token":"\([^"]*\)".*/\1/p')
echo "$TOKEN" > /opt/sonarqube/token.txt
chmod 666 /opt/sonarqube/token.txt
sync
wait
