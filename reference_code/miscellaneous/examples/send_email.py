from smtplib import SMTP
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.mail.com'
SMTP_SERVER_PORT = 587
E_FROM = 'XXX@mail.com'
E_TO = 'XXX@mail.com'
E_SUBJECT = 'test email (subject)'
E_CONTENT_TEXT = '''This is test email.
    This must be on the second line.'''
E_CONTENT_HTML = """<b style='color:red'>Bold red text</b>"""
MSG_TYPE = 'html' # plain

USER_NAME = 'XXX@mail.com'
USER_PASSWORD = 'XXX'

def send_email():
    msg = MIMEText(E_CONTENT_HTML, MSG_TYPE)
    msg['Subject'] = E_SUBJECT
    msg['From'] = E_FROM
    msg['To'] = E_TO
    try:
        conn = SMTP(host=SMTP_SERVER, port=SMTP_SERVER_PORT)
        #enable ESTMP (extra commands can be used, e.g. starttls)
        status_code = conn.ehlo()[0]
        if status_code != 250:
            print('ehlo response code: %s, exiting' % status_code)
            return
        status_code = conn.starttls()[0]
        if status_code != 220:
            print('starttls response code: %s, exiting' % status_code)
            return
        # ehlo called again as advice from smtplib documentation
        status_code = conn.ehlo()[0]
        if status_code != 250:
            print('ehlo response code: %s, exiting' % status_code)
            return
        conn.login(USER_NAME, USER_PASSWORD)
        try:
            conn.sendmail(E_FROM, E_TO, msg.as_string())
            print('Message sent successfully')
        finally:
            conn.quit()
    except Exception as exc:
        print("Mail failed: {}".format(exc))


if __name__ == "__main__":
    send_email()

