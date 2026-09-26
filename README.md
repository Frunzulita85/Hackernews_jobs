# 🧡 HackerNews Job Monitor & Email Notifier

A lightweight, automated Python script that monitors the official HackerNews Firebase API for new job postings, filters them based on custom preferences, and delivers structured HTML email notifications directly to your inbox.

Designed to run seamlessly as a background task via Windows Task Scheduler, Cron, or any server environment.

---

## 🚀 Key Features

- **Direct API Integration:** Queries the official HackerNews Firebase API (`jobstories.json` and item endpoints) for fast and reliable data fetching.
- **Smart Deduplication:** Keeps track of previously processed listing IDs in a local `seen_jobs.txt` file to prevent duplicate email alerts.
- **HTML Email Alerts:** Formats incoming jobs into clean, modern HTML emails with direct application links.
- **Automation Ready:** Works out-of-the-box with Windows Task Scheduler or Linux Cron jobs for hourly/daily automated runs.
- **Lightweight & Fast:** Uses native Python libraries (`smtplib`, `email`) and minimal external dependencies (`requests`).

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **HTTP Client:** `requests`
- **Email Delivery:** Python `smtplib` & `email.mime` (Gmail SMTP)
- **API:** Official HackerNews Firebase REST API

---

## 📁 Repository Structure

```text
Hackernews_jobs/
├── hn_jobs.py         # Main execution script
├── seen_jobs.txt      # Local database tracking processed job IDs (git-ignored)
├── .gitignore         # Prevents sensitive files and local state from being tracked
└── README.md          # Project documentation
