import smtplib
from email.message import EmailMessage
import sqlite3



while true:
    now = datetime.utcnow()
    if(now.minute == 15):
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM recipients")

        rows = cur.fetchall()
        email = []
        for row in rows:
            email.append(row[2])

        def email_alert(subject, body, to):
            msg = EmailMessage()
            msg.set_content(body)
            msg['subject'] = subject
            msg['to'] = to

            user = "airquality.notifications@gmail.com"
            msg['from'] = user
            password = "qnfhefizqzdaddfi"

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(user, password)
            server.send_message(msg)
            server.quit()

        for i in email:
            email_alert("Air quality alert", "Alert! The airquality is bad today", i)
