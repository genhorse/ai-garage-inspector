#!/usr/bin/env bash

# Pulling the model
echo "Pulling DeepSeek‑Coder model…"
until sudo docker exec ollama ollama pull deepseek-coder:1.3b; do
    sleep 5
done

# Waiting for readiness
echo "Waiting for the model to become usable…"
until curl -s -o /dev/null -w "%{http_code}" \
    -X POST http://localhost:11434/api/generate \
    -d '{"model":"deepseek-coder:1.3b","prompt":"ping","stream":false}' \
    | grep -q '^200$'; do
    sleep 10
done
echo "✅ System Active."
