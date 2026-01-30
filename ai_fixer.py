#!/usr/bin/env python3
import requests, json, sys, re, time

URL   = "http://ollama:11434/api/generate"
MODEL = "deepseek-coder:1.3b"
FILE_PATH = "garage-inspector/app/main.py"

MAX_RETRIES = 30          # ≈5 минут
WAIT_SECONDS = 10

def wait_for_model():
    payload = {"model": MODEL, "prompt": "ping", "stream": False}
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.post(URL, json=payload, timeout=30)
            if r.status_code == 200:
                return
            print(f"[{attempt}/{MAX_RETRIES}] Model not ready (status {r.status_code}), waiting {WAIT_SECONDS}s …")
        except Exception as e:
            print(f"[{attempt}/{MAX_RETRIES}] Exception while waiting for model: {e}")
        time.sleep(WAIT_SECONDS)
    print(f"❌ Model {MODEL} still not ready after {MAX_RETRIES * WAIT_SECONDS}s")
    sys.exit(1)

def fix_code():
    wait_for_model()          # <‑‑ ждём, пока модель будет готова
    with open(FILE_PATH, "r") as f:
        code = f.read()

    prompt = (
        f"Fix SonarQube 'identical expression' bugs in this Python code. "
        f"Keep references to 'Tesla' and '64 years old'. "
        f"Return ONLY raw code without markdown formatting. English comments only.\n\n"
        f"CODE:\n{code}"
    )
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.1}
    }

    try:
        r = requests.post(URL, json=payload, timeout=90)
        r.raise_for_status()
        new_code = r.json()["response"].strip()
        new_code = re.sub(r'```python|```', '', new_code).strip()
        if len(new_code) > 10:
            with open(FILE_PATH, "w") as f:
                f.write(new_code)
            print("✅ AI Fix applied.")
            sys.exit(0)
        else:
            print("⚠️ Received empty/too‑short response – nothing written.")
            sys.exit(1)
    except Exception as e:
        print(f"❌ AI Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fix_code()
