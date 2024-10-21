import os
import smtplib
import sys
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def convert_html_to_pdf(html_file, output_pdf):
    # Tu API Key de ConvertAPI como Bearer Token
    api_key = "secret_33Otwk7xGAueKYrd"  # Cambia esta clave por la tuya si es necesario

    # URL de la API de ConvertAPI para convertir HTML a PDF
    url = "https://v2.convertapi.com/convert/html/to/pdf"

    # Configuración de encabezados
    headers = {
        'Authorization': f"Bearer {api_key}"
    }

    # Parámetros para la conversión
    payload = {
        'StoreFile': 'true'
    }

    files = {
        'File': (html_file, open(html_file, 'rb'))
    }

    # Realizar la solicitud POST para convertir el HTML a PDF
    response = requests.post(url, headers=headers, data=payload, files=files)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        pdf_url = response.json()['Files'][0]['Url']
        pdf_response = requests.get(pdf_url)

        # Guardar el PDF descargado en un archivo local
        with open(output_pdf, 'wb') as pdf_file:
            pdf_file.write(pdf_response.content)
        print(f"PDF guardado en {output_pdf}")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

def send_email(subject):
    user = os.environ['EMAIL_USER']
    password = os.environ['EMAIL_PASS']
    recipients = os.environ['RECIPIENTS'].split(",")
    body = "Adjunto el informe de las pruebas ejecutadas."

    html_filename = "reportprueba.html"
    pdf_filename = "reportprueba.pdf"

    # Convertir HTML a PDF
    convert_html_to_pdf(html_filename, pdf_filename)

    # Crear el contenedor del mensaje
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Adjuntar el cuerpo del mensaje
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo HTML
    with open(html_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {html_filename}")
        msg.attach(part)

    # Adjuntar el archivo PDF
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {pdf_filename}")
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