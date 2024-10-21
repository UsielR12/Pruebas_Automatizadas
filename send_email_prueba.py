import os
import smtplib
import sys
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def convert_html_to_pdf(html_file, output_pdf):
    # Tu API Key de HTML2PDF Rocket
    api_key = "9e6657d4-9be3-458f-9751-3176de892cf5"

    # Leer el contenido HTML desde el archivo generado por pytest-html
    with open(html_file, 'r') as file:
        html_content = file.read()

    # URL de la API de HTML2PDF Rocket
    url = "https://html2pdfrocket.p.rapidapi.com/convert"

    # Configuración de parámetros para la conversión
    querystring = {
        "value": html_content,
        "apikey": api_key,
        "margin": "0"  # Ajusta los márgenes si es necesario
    }

    headers = {
        'x-rapidapi-host': "html2pdfrocket.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    # Realizar la solicitud GET para la conversión
    response = requests.get(url, headers=headers, params=querystring)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Guardar el PDF generado en un archivo local
        with open(output_pdf, 'wb') as pdf_file:
            pdf_file.write(response.content)
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