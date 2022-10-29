import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from yaml import safe_load


def send_mail(subject, bodymessage, from_addr, to_addr, server, port, user, password):
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
    msg.attach(
        MIMEText(
            '<html><body>' + '<p><img src="cid:0"></p>' + bodymessage + '</body></html>', 'html', 'utf-8'
        )
    )

    server = smtplib.SMTP(server, port)
    server.set_debuglevel(1)
    server.login(
        user,
        password
    )
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()


def get_config():
    """ Reads a config from a YAML file."""
    current_file = Path(__file__).resolve()
    root_dir = current_file.parents[0]
    config_file = root_dir / 'config/config.yaml'
    with open(config_file, "r") as yml_config:
        config = safe_load(yml_config)
    return config
