import os
import smtplib
import pdfcrowd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def convert_html_to_pdf(input_html, output_pdf):
    """Convierte un archivo HTML a PDF usando la API de PDFCrowd."""
    try:
        # Crear el cliente de conversión
        client = pdfcrowd.HtmlToPdfClient(os.environ['PDFCROWD_USER'], os.environ['PDFCROWD_API_KEY'])

        # Leer el contenido del archivo HTML
        with open(input_html, 'r') as file:
            html_content = file.read()

        # Convertir el contenido HTML a PDF
        with open(output_pdf, 'wb') as output_file:
            client.convertStringToFile(html_content, output_pdf)

        print("PDF generado correctamente.")
    except pdfcrowd.Error as e:
        print(f"Error durante la conversión a PDF: {e}")
        raise


def send_email(subject):
    user = os.environ['EMAIL_USER']
    password = os.environ['EMAIL_PASS']
    recipients = os.environ['RECIPIENTS'].split(",")
    body = "Adjunto el informe de las pruebas ejecutadas."
    input_html = "reportprueba.html"
    output_pdf = "reportprueba.pdf"

    # Convertir el archivo HTML a PDF
    convert_html_to_pdf(input_html, output_pdf)

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
    subject = "Reporte de pruebas"
    send_email(subject)