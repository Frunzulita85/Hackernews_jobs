# 🧡 HackerNews Job Monitor & Email Notifier

A lightweight, automated Python script that monitors the official HackerNews Firebase API for new job postings, filters them based on custom preferences, and delivers structured HTML email notifications directly to your inbox.

Designed to run seamlessly as a background task via Windows Task Scheduler, Cron, or any server environment.

---

## 🚀 Key Features

- Direct API Integration: Queries the official HackerNews Firebase API (jobstories.json and item endpoints) for fast and reliable data fetching.
- Smart Deduplication: Keeps track of previously processed listing IDs in a local seen_jobs.txt file to prevent duplicate email alerts.
- HTML Email Alerts: Formats incoming jobs into clean, modern HTML emails with direct application links.
- Automation Ready: Works out-of-the-box with Windows Task Scheduler or Linux Cron jobs for hourly/daily automated runs.
- Lightweight & Fast: Uses native Python libraries (smtplib, email) and minimal external dependencies (requests).

---

## 🛠️ Tech Stack

- Language: Python 3.10+
- HTTP Client: requests
- Email Delivery: Python smtplib & email.mime (Gmail SMTP)
- API: Official HackerNews Firebase REST API

---

## 📁 Repository Structure

Hackernews_jobs/
├── hn_jobs.py         # Main execution script
├── seen_jobs.txt      # Local database tracking processed job IDs (git-ignored)
├── .gitignore         # Prevents sensitive files and local state from being tracked
└── README.md          # Project documentation

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
git clone https://github.com/Frunzulita85/Hackernews_jobs.git
cd Hackernews_jobs

### 2. Install Dependencies
pip install requests

### 3. Configure Environment Credentials
For security reasons, never hardcode passwords directly into the script. Set your Google App Password as an environment variable or update hn_jobs.py using placeholder values:

SENDER_EMAIL = "your-email@gmail.com"
RECEIVER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = os.getenv("GMAIL_APP_PASSWORD", "YOUR_GMAIL_APP_PASSWORD")

Note: To send emails via Gmail SMTP, generate an App Password from your Google Account settings under Security > 2-Step Verification > App Passwords.

---

## 🏃 Usage

Run the script manually from the command line:

python hn_jobs.py

### Automated Execution (Windows Task Scheduler)
To run this script automatically every hour on Windows:
1. Open Task Scheduler and click Create Basic Task.
2. Set Trigger to Daily, repeating every 1 hour.
3. Set Action to Start a Program:
   - Program/script: Path to your python.exe
   - Add arguments: hn_jobs.py
   - Start in (crucial): Full path to your local project directory (e.g., C:\Python projects\Hackernewsjobs)

---

## 📝 License

Distributed under the MIT License. See LICENSE for more information.

---

## 👤 Author

Frunză Călin
- GitHub: @Frunzulita85
- Product Portfolio: LeadAtlas.io
