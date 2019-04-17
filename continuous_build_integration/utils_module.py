import smtplib
import os
import configparser
from shutil import copy
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
from email.mime.base import MIMEBase
from email import encoders

COMMASPACE = ', '


# Setting the config python parser
config = configparser.ConfigParser()
config.read('config.ini')


# This function is used in cases where there is an existing folder that
# can contains both folders and files. All will be overwritten but nothing deleted
# Used in the Qt libraries copy.
def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f),
                                    os.path.join(dest, f),
                                    ignore)
    else:
        copy(src, dest)


# Get error lines form the stdout
def get_error_lines():

    f = open("outfile.txt", "r")
    lista_folders = set([])
    error = False
    for line in f.readlines():
        # lista.append(line)
        if "error" in line:
            error = True
            line = line.replace('\\', '/')
            line = line[line.find('/'):]
            m = re.search(r'^\/[^/]+\/([^/]+)\/', line)
            if m:
                if m not in lista_folders:
                    if m.group(1):
                        lista_folders.add(m.group(1))
    attached(error, lista_folders)


# Send error lines and result of build by mail
def send_mail(error):

    gmail_user = 'terrabld.tas@gmail.com'

    # PASSWORD MUST BE KNOWN BY THE USER AND SET IN CONFIG.INI
    gmail_app_password = config['DEFAULTS']['passwordMailAddress']
    sent_from = gmail_user
    sent_to = [config['DEFAULTS']['mailAddressBuildResults']]
    if error:
        sent_subject = "Error"
    else:
        sent_subject = "No error"
    sent_body = ("Check attached if building failed\n\n" + g.read())

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)


def attached(error, lista_folders):
    sender = 'terrabld.tas@gmail.com'
    # PASSWORD MUST BE KNOWN BY THE USER AND SET IN CONFIG.INI
    gmail_password = config['DEFAULTS']['passwordMailAddress']
    recipients = [config['DEFAULTS']['mailAddressBuildResults']]

    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    text = ""
    if error:
        outer['Subject'] = 'TerRaSys build failed. Check attached'
        text = "Errors found in the following projects: \n\n"
    else:
        outer['Subject'] = 'TerRaSys build finished successfully!'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    for folder in lista_folders:
        text += folder + '\n'
    outer.attach(MIMEText(text, 'plain'))
    # List of attachments
    attachments = ['outfile.txt']

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except Exception as exception:
            print("Error: %s!\n\n" % exception)
            raise

    composed = outer.as_string()

    # Send the email
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, gmail_password)
        server.sendmail(sender, recipients, composed)
        server.close()
        print("Email sent!")
    except Exception as exception:
        print("Error: %s!\n\n" % exception)
        raise


if __name__ == '__attached__':
    attached()


