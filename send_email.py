import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from playwright.sync_api import sync_playwright

def convert_html_to_pdf(input_html, output_pdf):
    """Convierte un archivo HTML en PDF usando Playwright, asegurándose de que el contenido dinámico se cargue."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Cargar el contenido HTML
        with open(input_html, 'r') as file:
            html_content = file.read()

        page.set_content(html_content)

        # Esperar a que todos los elementos y scripts se carguen (puedes ajustar el timeout si es necesario)
        page.wait_for_load_state('networkidle')  # Espera a que no haya más tráfico de red (carga de JS)

        # Generar el PDF con todos los detalles
        page.pdf(path=output_pdf, format='A4', print_background=True)

        browser.close()

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