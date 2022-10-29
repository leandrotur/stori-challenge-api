import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path


def send_mail(subject, bodymessage, from_addr, to_addr):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    text = MIMEText('<img src="cid:image1">', 'html')
    msg.attach(text)
    current_path = Path(__file__).resolve().parent
    f = open(f'{current_path}/logo.png', 'rb')
    # set attachment mime and file name, the image type is png
    mime = MIMEBase('image', 'png', filename='logo.png')
    # add required header data:
    mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
    mime.add_header('X-Attachment-Id', '0')
    mime.add_header('Content-ID', '<0>')
    # read attachment file content into the MIMEBase object
    mime.set_payload(f.read())
    # encode with base64
    encoders.encode_base64(mime)
    # add MIMEBase object to MIMEMultipart object
    msg.attach(mime)
    msg.attach(MIMEText(
        '<html><body>' + '<p><img src="cid:0"></p>' + bodymessage
        + '</body></html>', 'html', 'utf-8'
        )
    )

    server = smtplib.SMTP('smtp.mailgun.org', 587)
    server.set_debuglevel(1)
    server.login(
        'postmaster@sandboxc316f4780cb14a5d9fcc134593de8d0e.mailgun.org',
        'c2ef9814b21d88a80681ace5d2b0a522-73e57fef-d7834906'
    )
    server.sendmail('leandroturdera1982@gmail.com', to_addr, msg.as_string())
    server.quit()
