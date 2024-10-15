import os
import smtplib
import sys
import pdfkit
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def convert_html_to_pdf(input_html, output_pdf):
    """Convierte un archivo HTML en un PDF."""
    try:
        pdfkit.from_file(input_html, output_pdf)
        print(f"Archivo PDF generado: {output_pdf}")
    except Exception as e:
        print(f"Error al convertir HTML a PDF: {e}")
        sys.exit(1)

def send_email(subject):
    user = os.environ['EMAIL_USER']
    password = os.environ['EMAIL_PASS']
    recipients = os.environ['RECIPIENTS'].split(",")
    body = "Adjunto el informe de las pruebas ejecutadas."
    input_html = "reportprueba.html"
    output_pdf = "reportprueba.pdf"

    # Convertir el archivo HTML a PDF
    convert_html_to_pdf(input_html, output_pdf)

    # Verificar si el PDF se generó correctamente antes de enviar el correo
    if not os.path.exists(output_pdf):
        print(f"El archivo PDF no fue encontrado: {output_pdf}")
        sys.exit(1)

    # Crear el contenedor del mensaje
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Adjuntar el cuerpo del mensaje
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo PDF
    with open(output_pdf, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {output_pdf}")
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