import os
import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def convert_html_to_pdf(html_content, output_pdf):
    api_key = "fb99005ce15cd9ecbca33c72ff994556"
    url = f"http://api.pdflayer.com/api/convert?access_key={api_key}"

    payload = {
        'document_html': html_content,
        'css_url': '',
        'title': 'Informe de Pruebas',
        'margin_top': '0',
        'margin_bottom': '0',
        'margin_left': '0',
        'margin_right': '0'
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        with open(output_pdf, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"PDF guardado en {output_pdf}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


def send_email(subject, output_pdf):
    user = os.environ['EMAIL_USER']
    password = os.environ['EMAIL_PASS']
    recipients = os.environ['RECIPIENTS'].split(",")
    body = "Adjunto el informe de las pruebas ejecutadas."

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with open(output_pdf, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {output_pdf}")
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    text = msg.as_string()
    server.sendmail(user, recipients, text)
    server.quit()


if __name__ == "__main__":
    with open('reportprueba.html', 'r') as file:
        html_content = file.read()

    output_pdf = 'reportprueba.pdf'

    # Convertir el HTML a PDF
    convert_html_to_pdf(html_content, output_pdf)

    # Enviar el PDF por correo
    send_email("Informe de Pruebas Automatizadas", output_pdf)