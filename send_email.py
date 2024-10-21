import os
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject):
    user = os.environ['EMAIL_USER']
    password = os.environ['EMAIL_PASS']
    recipients = os.environ['RECIPIENTS'].split(",")
    body = "Adjunto el informe de las pruebas ejecutadas."
    filename = "reportprueba.html"

    # Crear el contenedor del mensaje
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Adjuntar el cuerpo del mensaje
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo
    with open(filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)

    # Iniciar sesión en el servidor y enviar el correo
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    text = msg.as_string()
    server.sendmail(user, recipients, text)
    server.quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: send_email.py <subject>")
        sys.exit(1)

    subject = sys.argv[1]
    send_email(subject)