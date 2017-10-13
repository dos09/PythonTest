
USE_SSL = True #otherwise it is TLS

if USE_SSL:
    from smtplib import SMTP_SSL as SMTP
    print('Imported SMTP_SSL')
else:
    from smtplib import SMTP
    print('Imported SMTP')
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmx.com'#'smtp.mail.com'
SMTP_SERVER_PORT = 465 # for mail.com 587, for gmx.com 465
E_FROM = 'FromXX <X@gmx.com>'
E_TO = 'ToXX <X@gmx.com>'
E_SUBJECT = 'test email (subject)'
E_CONTENT_TEXT = '''This is test email.
    This must be on the second line.'''
E_CONTENT_HTML = """<b style='color:red'>Bold red text</b>"""
MSG_TYPE = 'html' # plain

USER_NAME = 'X@gmx.com'
USER_PASSWORD = 'X'

def send_email():
    # the email headers msg['XXX] must be strings
    # if list join with comma
    msg = MIMEMultipart('alternative')
    msg['Subject'] = E_SUBJECT
    msg['From'] = E_FROM
    msg['To'] = E_TO
    cc = ['F@gmx.com']
    msg['CC'] = ','.join(cc)
    recipients = [E_TO] + cc
    part1 = MIMEText(E_CONTENT_TEXT, 'plain')
    # smtp servers chop lines longer than 990 symbols and insert new line
    # which can corrupt html, can use fix_html from reusable_code directory
    part2 = MIMEText(E_CONTENT_HTML, 'html')
    msg.attach(part1)
    msg.attach(part2)
    
    # if we send only one type of data
#     msg = MIMEText(E_CONTENT_HTML, MSG_TYPE)
#     msg['Subject'] = E_SUBJECT
#     msg['From'] = E_FROM
#     msg['To'] = E_TO
    try:
        conn = SMTP(host=SMTP_SERVER, port=SMTP_SERVER_PORT)
        #enable ESTMP (extra commands can be used, e.g. starttls)

        if not USE_SSL:
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
            conn.sendmail(E_FROM, recipients, msg.as_string())
            print('Message sent successfully')
        finally:
            conn.quit()
    except Exception as exc:
        print("Mail failed: {}".format(exc))


if __name__ == "__main__":
    send_email()

# when sending html must have '\r\n' to split long lines (900+ symbols))