import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os
import mimetypes


class myMail:
    def __init__(self, host, port, user, password, to_addr, subject, content, attach):
        self.smtp = smtplib.SMTP()
        self.msg = None
        self.host = host
        self.port = port
        self.login_user = user
        self.login_password = password
        self.from_addr = user + '@163.com'
        self.to_addr = to_addr
        self.mail_attach_path = attach
        self.mail_subject = subject
        self.mail_content = content

    def connect(self):
        self.smtp.connect(self.host, self.port)

    def login(self):
        self.smtp.login(self.login_user, self.login_password)
        print("登陆成功")

    def make_msg(self):
        self.msg = MIMEMultipart()
        self.msg['From'] = self.from_addr
        self.msg['To'] = ','.join(self.to_addr)
        self.msg['Subject'] = self.mail_subject
        self.msg.attach(MIMEText(self.mail_content, 'plain', 'utf-8'))

    def attach_msg(self):
        if self.mail_attach_path != None:
            for attachment_path in self.mail_attach_path:
                if os.path.isfile(attachment_path):
                    type, coding = mimetypes.guess_type(attachment_path)
                    if type == None:
                        type = 'application/octet-stream'
                    major_type, minor_type = type.split('/', 1)
                    if major_type == 'text':
                        attachment = MIMEText(open(attachment_path, 'rb').read(), 'base64', 'utf-8')
                    elif major_type == 'image':
                        attachment = MIMEImage(open(attachment_path, 'rb').read(), _subtype=minor_type)
                    elif major_type == 'application':
                        attachment = MIMEApplication(open(attachment_path, 'rb').read(), _subtype=minor_type)
                    elif major_type == 'audio':
                        attachment = MIMEAudio(open(attachment_path, 'rb').read(), _subtype=minor_type)

                    attachment_name = os.path.basename(attachment_path)
                    attachment.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', attachment_name))
                    self.msg.attach(attachment)

    def send_mail(self):
        self.smtp.sendmail(self.from_addr, self.to_addr, self.msg.as_string())
        print("success")
        self.smtp.quit()

    def run(self):
        self.connect()
        self.login()
        self.make_msg()
        self.attach_msg()
        self.send_mail()
