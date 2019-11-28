from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from data.resources.emails.templates import templates
from smtplib import SMTP
from config.settings import config

class Email():
    def __init__(self, template, **kwargs):
        self.template = templates[template]
        self.subject = self.replace_values(self.template['subject'], **kwargs)
        self.plaintext = self.replace_values(self.template['plaintext'], **kwargs)
        self.html = self.replace_values(self.template['html'], **kwargs)

    def replace_values(self, input, **kwargs):
        """Replace keyword arguments (e.g. "[student_name]") with their corresponding values"""
        output = input
        for arg in kwargs:
            try:
                replacement_text = kwargs[arg]
            except KeyError:
                replacement_text = ''
            output = output.replace('['+arg+']', replacement_text)
        return output

    def send(self, to_addr):
        debuglevel = False # True to print debug messages
        smtp = SMTP()
        smtp.set_debuglevel(debuglevel)
        try:
            connection = smtp.connect(config["email"]["server_addr"], config["email"]["port"])
            login = smtp.login(config["email"]["username"], config["email"]["password"])
        except Exception as e:
            print("Error setting up email: ", e)
            raise

        sender = config["email"]["from_addr"]
        to = to_addr
        server = config["email"]["server_addr"]

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = sender
        msg['To'] = to

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(self.plaintext.encode('utf-8'), 'plain', 'utf-8')
        part2 = MIMEText(self.html.encode('utf-8'), 'html', 'utf-8')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part1)
        msg.attach(part2)

        # Send the message.
        try:
            smtp.sendmail(sender, [to], msg.as_string())
        except Exception as e:
            print("Error sending email: ", e)
        finally:
            smtp.quit()
