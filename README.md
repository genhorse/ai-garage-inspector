# AI Garage Inspector v1.18 (TOTAL AUTO-REMEDIATION) 🤖🚀
### Automated Self-Healing CI/CD Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 PROJECT OVERVIEW
This project implements a high-level **Self-Healing CI/CD Pipeline**. It demonstrates the integration of static code analysis (**SonarQube**) with a local LLM (**DeepSeek-Coder via Ollama**) to automatically identify and fix technical debt.

The system currently monitors a Python-based FastAPI application—which serves as a functional **placeholder** for the upcoming **Neo 512M** core engine—and uses AI to perform real-time code patches without human intervention.

## 🏗 PROJECT CONCEPT & NAMING
The name **"AI Garage Inspector"** represents the evolution of this portfolio:
* **v1.18 (Current):** "The Infrastructure". Focus on AI-driven CI/CD using a Python placeholder.
* **v2.0 (Next):** "The Ecosystem". Adding Jira auto-ticketing and Grafana dashboards.
* **v3.0 (Goal):** "The Real Deal". Full migration of placeholders to the **Neo 512M** core — a specialized application for garage inventory and part inspection.

## 💻 DEVELOPMENT ENVIRONMENT (WSL2)
* **OS:** Windows 11 + WSL2 (Ubuntu 24.04 LTS)
* **Docker:** Engine version 24+
> ⚠️ **CRITICAL:** Do NOT clone this repository into the Windows host filesystem (`/mnt/c/...`). Due to Docker's handling of Linux permissions and volume mounts, you must use the native WSL2 home directory (e.g., `~/projects/`) to ensure all services (like SonarQube) work correctly.

## 🧠 AI ENGINE & VISUAL PROOF
This project runs a local **DeepSeek-Coder-1.3b** model. Visual documentation in the Wiki includes three key proofs:
1. `sonar_issues.png` — Real-time bug detection.
2. `jenkins_pipeline.png` — The automated healing sequence.
3. `ollama_logs.png` — AI processing logs showing the model in action.

## 🛠 TECH STACK
* **Orchestration:** Jenkins (JCasC, Job-DSL)
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
├── setup_ai.sh             # Model downloader and health-check
└── sonar-init/             # SonarQube customization & auto-provisioning
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
2. **Issue Detection:** If bugs are found, the build moves to **AI Remediation**.
3. **AI Fix:** `ai_fixer.py` sends the buggy code to DeepSeek-Coder with strict instructions (English comments only, preserve business logic like "Tesla" and "64 years old").
4. **Auto-Patch:** The AI-corrected code overwrites the local file.
5. **Verification:** Jenkins triggers a second build automatically. If the new scan is clean, the pipeline turns **GREEN**.

## 🧠 WIKI & DOCUMENTATION
For a deeper dive into the architecture and visual proofs, please visit the **Project Wiki**.

---
**Author:** 2026 Developer Portfolio Project.  
*Note: All code comments and AI-generated outputs are strictly in English.*
