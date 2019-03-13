import smtplib


def get_error_lines():
    f = open("outfile", "r")
    g = open("toMail.txt", "w")
    lista = []
    for line in f.readlines():
        lista.append(line)
        if "error" in line:
            error = True
            g.write(line)
    g.write(lista[-1] + "\n" + lista[-2])
    g.close()
    get_error_and_send_mail(error)


def get_error_and_send_mail(error):
    g = open("toMail.txt", "r")
    gmail_user = 'terrabld.tas@gmail.com'
    gmail_app_password = 'terrabldtas'
    sent_from = 'terrabld.tas'
    sent_to = ['julio.calvo@itu.int']
    if not error:
        sent_subject = "Successful Building execution"
    else:
        sent_subject = "Building execution failed"
    sent_body = g.read()
    email_text = """\
    From: %s 
    Subject: %s 

    %s """ % (sent_from, sent_subject, sent_body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)










