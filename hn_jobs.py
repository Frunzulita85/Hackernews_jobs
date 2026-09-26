import requests
import datetime
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ================= CONFIGURARE E-MAIL =================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your password"  # App Password generată din contul Google
RECIPIENT_EMAIL = "your_email@gmail.com"  # Unde vrei să primești alertele

SEEN_JOBS_FILE = "seen_jobs.txt"


# ================= FUNCȚII AJUTĂTOARE =================
def load_seen_jobs():
    """Încarcă ID-urile job-urilor deja procesate pentru a evita duplicatele."""
    if not os.path.exists(SEEN_JOBS_FILE):
        return set()
    with open(SEEN_JOBS_FILE, "r") as f:
        return set(line.strip() for line in f if line.strip())


def save_seen_job(job_id):
    """Salvează ID-ul unui job nou procesat în fișierul local."""
    with open(SEEN_JOBS_FILE, "a") as f:
        f.write(f"{job_id}\n")


def send_email_notification(job_title, job_url, job_date):
    """Trimite un e-mail HTML frumos formatat cu detaliile job-ului."""
    subject = f"🚨 Job Nou HackerNews: {job_title[:50]}..."

    # Corpul e-mail-ului în format HTML
    html_content = f"""
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px;">
          <h2 style="color: #ff6600; margin-top: 0;">📌 Job Nou pe HackerNews</h2>
          <p><strong>Titlu:</strong> {job_title}</p>
          <p><strong>Data postării:</strong> {job_date}</p>
          <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
          <a href="{job_url}" style="background-color: #ff6600; color: white; padding: 10px 18px; text-decoration: none; border-radius: 4px; display: inline-block; font-weight: bold;">Vezi Anunțul & Aplică</a>
        </div>
      </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print(f"📧 E-mail trimis cu succes pentru: {job_title}")
    except Exception as e:
        print(f"❌ Eroare la trimiterea e-mail-ului: {e}")


# ================= VERIFICARE HACKERNEWS =================
def check_hn_jobs(keyword=None, limit=20):
    print("🔄 Verificăm ultimele job-uri pe HackerNews...")
    seen_jobs = load_seen_jobs()

    # Preia ID-urile ultimelor job-uri de pe API-ul oficial HackerNews
    job_ids_url = "https://hacker-news.firebaseio.com/v0/jobstories.json"
    response = requests.get(job_ids_url)

    if response.status_code != 200:
        print("A apărut o eroare la conectarea cu HackerNews API.")
        return

    job_ids = response.json()[:limit]

    for job_id in job_ids:
        str_job_id = str(job_id)

        # Sărim peste job-urile pe care le-am trimis deja pe e-mail
        if str_job_id in seen_jobs:
            continue

        item_url = f"https://hacker-news.firebaseio.com/v0/item/{job_id}.json"
        job = requests.get(item_url).json()

        if not job:
            continue

        title = job.get("title", "Fără titlu")
        url = job.get("url", f"https://news.ycombinator.com/item?id={job_id}")
        timestamp = job.get("time")
        date_str = datetime.datetime.fromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M') if timestamp else "N/A"

        # Filtrare opțională după cuvânt cheie
        if keyword and keyword.lower() not in title.lower():
            continue

        # Trimitem e-mail-ul și salvăm ID-ul pentru a evita duplicatele
        send_email_notification(title, url, date_str)
        save_seen_job(str_job_id)


if __name__ == "__main__":
    # Setează un cuvânt cheie (ex: "remote", "python", "backend")
    # Sau pune KEYWORD = None pentru a le primi pe toate
    KEYWORD = None

    check_hn_jobs(keyword=KEYWORD, limit=20)
