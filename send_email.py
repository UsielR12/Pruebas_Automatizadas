import os
import yagmail

def send_email():
    user = os.environ['EMAIL_USER']
    password = os.environ['EMAIL_PASS']
    recipient = os.environ['RECIPIENT']
    subject = "Informe de pruebas automatizadas"
    body = "Adjunto el informe de las pruebas ejecutadas."
    filename = "reportprueba.html"

    yag = yagmail.SMTP(user, password)
    yag.send(
        to=recipient,
        subject=subject,
        contents=[body, yagmail.inline(filename)],
    )

if __name__ == "__main__":
    send_email()