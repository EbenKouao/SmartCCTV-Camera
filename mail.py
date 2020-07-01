import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Email you want to send the update from (only works with gmail)
fromEmail = ''

# You can generate an app password here to avoid storing your password in plain text
# https://support.google.com/accounts/answer/185833?hl=en
fromEmailPassword = ''

# Email you want to send the update to
toEmail = ''

def sendEmail():
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'SmartCCTV - Eben is at the door'
    msgRoot['From'] = fromEmail
    msgRoot['To'] = toEmail
    msgRoot.preamble = 'SmartCCTV Update'

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    msgText = MIMEText('SmartCCTV not found')
    msgAlternative.attach(msgText)

    msgText = MIMEText('<a href="eben.ddns.net">View SmartCCTV Live Feed</a>', 'html')
    msgAlternative.attach(msgText)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(fromEmail, fromEmailPassword)
    smtp.sendmail(fromEmail, toEmail, msgRoot.as_string())
    smtp.quit()
    
sendEmail()
