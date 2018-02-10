from smtplib import SMTP_SSL, SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from collections import namedtuple

EmailConfig = namedtuple('EmailConfig',
                         'server port email_from password is_ssl')

LOG = logging.getLogger(__name__)


class EmailSender:

    def __init__(self, email_config):
        self.email_config = email_config
        self.conn = EmailSender.get_email_connection(email_config)

    def send_email(self, e_to, e_subject,
                   e_body_text=None, e_body_html=None, e_cc=None,
                   retry_once=False):
        """ Return True on successful sending, False on failure. 

        - e_to and e_cc can be of data type string or list of strings.
        - retry_once: if the connection is dropped on failing to send the email
        will try to establish new connection and will retry the sending
        """

        # - when sending html:
        #   smtp servers chop lines longer than 990 symbols and insert new line
        #   which can corrupt html, can use fix_html method to fix that
        # - the email headers msg['XXX] must be strings

        if e_body_text is None and e_body_html is None:
            LOG.warning('Will send empty email')

        msg = MIMEMultipart('alternative')
        msg['Subject'] = e_subject
        e_from = self.email_config.email_from
        msg['From'] = e_from

        if isinstance(e_to, str):
            msg['To'] = e_to
            recipients = [e_to]
        else:
            msg['To'] = ','.join(e_to)
            recipients = e_to

        if e_cc:
            if isinstance(e_cc, str):
                msg['CC'] = e_cc
                e_cc = [e_cc]
            else:
                msg['CC'] = ','.join(e_cc)

            recipients.extend(e_cc)

        if e_body_text is not None:
            msg.attach(MIMEText(e_body_text, 'plain'))

        if e_body_html is not None:
            msg.attach(MIMEText(e_body_html, 'html'))

        if retry_once:
            return self._send_email_retry_once(e_from, e_to, recipients, msg)
        else:
            return self._send_email(e_from, e_to, recipients, msg)

    def _send_email(self, e_from, e_to, recipients, msg):
        """ Return True on successful sending, False on failure. """

        try:
            self.conn.sendmail(e_from, recipients, msg.as_string())
            LOG.info('Message to %s was sent successfully', e_to)
            return True
        except SMTPException as exc:
            LOG.warning("Mail sending to %s failed", e_to)
            LOG.warning(ex)

        return False

    def _send_email_retry_once(self, e_from, e_to, recipients, msg):
        """ Try to send an email, if the connection is dropped try to reconnect

        Return True on successful sending, False on failure.
        """

        exception_obj = None

        for attempt_number in range(2):
            try:
                self.conn.sendmail(e_from, recipients, msg.as_string())
                LOG.info('Message to %s was sent successfully', e_to)
                return True
            except SMTPServerDisconnected as ex_sd:
                if attempt_number == 1:  # second time
                    exception_obj = ex_sd
                    break

                LOG.info("Retrying to connect to the email server")
                self.conn = EmailSender.get_email_connection(self.email_config)
                if not self.conn:
                    LOG.warning('Failed to connect to the email server')
                    return False

            except SMTPException as ex:
                exception_obj = ex
                break

        LOG.warning("Mail sending to %s failed", e_to)
        LOG.warning(exception_obj)
        return False

    @staticmethod
    def get_email_connection(email_config):
        LOG.debug('Getting email connection')
        smtp_con_data = {
            'host': email_config.server,
            'port': email_config.port
        }

        if email_config.is_ssl:
            LOG.debug('Using SSL')
            conn = SMTP_SSL(**smtp_con_data)
        else:
            LOG.debug('Using TLS')
            conn = SMTP(**smtp_con_data)
            # activate TLS
            # enable ESTMP (extra commands can be used, e.g. starttls)
            status_code = conn.ehlo()[0]
            if status_code != 250:
                LOG.error('ehlo response code: %s, sending failed (1)',
                          status_code)
                return None
            status_code = conn.starttls()[0]
            if status_code != 220:
                LOG.error('starttls response code: %s, sending failed',
                          status_code)
                return None
            # ehlo called again as advice from smtplib documentation
            status_code = conn.ehlo()[0]
            if status_code != 250:
                LOG.error('ehlo response code: %s, sending failed (2)',
                          status_code)
                return None

        e_from = email_config.email_from
        username = EmailSender.extract_email_address(e_from)
        if not username:
            LOG.error('Failed to extract email from %s', e_from)
            return None

        LOG.debug('Sender: %s', username)
        conn.login(username, email_config.password)

        return conn

    @staticmethod
    def extract_email_address(email):
        email = email or ''
        s = email.find('<')
        e = email.rfind('>')

        if s != -1 and e != -1:
            return email[s + 1:e]

        if ' ' not in email:
            return email

        return None

    @staticmethod
    def fix_html(html):
        fixed = []
        for chunk in chop_str(html):
            fixed.append(insert_crlf(chunk))
        return ''.join(fixed)

    @staticmethod
    def _chop_str(str_data, chunk_width=500):
        chunks = []
        for i in range(0, len(str_data), chunk_width):
            chunks.append(str_data[i:i + chunk_width])
        return chunks

    @staticmethod
    def _insert_crlf(input_str):
        """ Inserts "\r\n" in input_str on appropriate place.

        Appropriate place is considered before "</" or  after "/>".
        If no such place is found tries to insert before a space.
        Search is from end to start.
        If there is no suitable insertion position the input_str is
        returned unmodified.
        """
        pos = input_str.rfind('</')
        if pos == -1:
            pos = input_str.rfind('/>')
            if pos == -1:
                pos = input_str.rfind(' ')
            else:
                pos += 2

        if pos != -1:
            return ''.join([input_str[:pos], '\r\n', input_str[pos:]])

        return input_str


def test_email_sending_to_self():
    """ Test sending an email to self (the address specified in the email.from)
        Required structure for the test .json file
        {
            "email": {
                "server": "X",
                "port": "X",
                "from": "X",
                "password": "X",
                "is_ssl": "false"
            }
        }
    """

    import os
    import json

    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter(
        "[%(asctime)s] [%(levelname)8s] --- %(message)s "
        "(%(filename)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S"))
    LOG.addHandler(ch)
    LOG.setLevel('DEBUG')

    filename = 'email.json'
    if not os.path.exists(filename):
        print('%s not found' % filename)
        return

    json_config = json.load(open(filename))
    email_config = EmailConfig(
        server=json_config['email']['server'],
        port=json.loads(json_config['email']['port']),
        email_from=json_config['email']['from'],
        password=json_config['email']['password'],
        is_ssl=json.loads(json_config['email']['is_ssl']))
    e_to = EmailSender.extract_email_address(email_config.email_from)
    if not e_to:
        print('Failed to get e_to')
        return

    e_subject = 'email utils'
    e_body_text = None
    e_body_html = None
    e_cc = None
    retry_once = False
    email_sender = EmailSender(email_config)
    email_sender.send_email(e_to=e_to,
                            e_subject=e_subject,
                            e_body_text=e_body_text,
                            e_body_html=e_body_html,
                            e_cc=e_cc,
                            retry_once=retry_once)
    print('done')

if __name__ == '__main__':
    test_email_sending_to_self()
