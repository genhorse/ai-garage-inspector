# ----------------------------------------------------------------------
# AI Garage Inspector v1.18 (TOTAL AUTO-REMEDIATION)
# ----------------------------------------------------------------------

## 📌 PROJECT OVERVIEW
This project is a high-level **Self-Healing CI/CD Pipeline**. It demonstrates how to integrate static code analysis with a local LLM to automatically fix technical debt and bugs.

The system targets a Python-based FastAPI application (current placeholder for the **Neo 512M** project) and uses **DeepSeek-Coder** to perform real-time code patches without human intervention.

## 🛠 TECH STACK
* **Orchestration:** Jenkins (Configuration as Code, Job-DSL)
* **Static Analysis:** SonarQube LTS
* **AI Engine:** Ollama + DeepSeek-Coder:1.3b (Local execution)
* **Backend:** Python (FastAPI)
* **Infrastructure:** Docker, Docker Compose, Bash

## 📂 REPOSITORY STRUCTURE
```text
.
├── ai_fixer.py           # Bridge between SonarQube API and Ollama
├── build-env/            # Custom Jenkins image & JCasC configs
├── docker-compose.yml    # Full stack definition
├── garage-inspector/     # App source code & Jenkinsfile
├── init.groovy.d/        # Jenkins auto-trigger scripts
├── setup_ai.sh           # Model downloader and health-check
└── sonar-init/           # SonarQube customization & auto-provisioning
```

## 🚀 QUICK START (LOCAL DEPLOYMENT)

### 1. Launch Infrastructure
Execute Docker Compose to build and start all services (Jenkins, SonarQube, Ollama):
```bash
echo "empty" > sonar_token.txt && chmod 666 sonar_token.txt
sudo docker compose up -d --build
```

### 2. Initialize AI Agent
Run the setup script to pull the 1.3b model and wait for the API to be ready:
```bash
chmod +x setup_ai.sh
./setup_ai.sh
```

### 3. Access the Tools
* **Jenkins:** `http://localhost:8080` (admin/admin)
* **SonarQube:** `http://localhost:9000` (admin/admin123)

## 🔄 PIPELINE WORKFLOW (THE "AUTO-PILOT")
1. **Quality Scan:** Jenkins triggers SonarQube to analyze `main.py`.
2. **Issue Detection:** If "Identical Expression" or other bugs are found, the build moves to **AI Remediation**.
3. **AI Fix:** `ai_fixer.py` sends the buggy code to DeepSeek-Coder with strict instructions (English comments only, preserve business logic like "Tesla" and "64 years old").
4. **Auto-Patch:** The AI-corrected code overwrites the local file.
5. **Verification:** Jenkins triggers a second build automatically. If the new scan is clean, the pipeline turns **GREEN**.



## 🧠 WIKI & DOCUMENTATION
For a deeper dive into the architecture, sequence diagrams, and visual proofs (screenshots), please visit the **Project Wiki** (coming soon).

## 📝 FUTURE ROADMAP
* **v2.0:** Jira Integration (auto-ticketing) & Grafana Dashboards for pipeline metrics.
* **v3.0:** Full migration of Python placeholders to the **Neo 512M** core engine.

---
**Author:** 2026 Developer Portfolio Project.  
*Note: All code comments and AI-generated outputs are strictly in English.*
