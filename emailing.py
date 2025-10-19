import smtplib
from email.message import EmailMessage
import imghdr

password = "bpvjrtrwsxonnqjz"
sender = "luffynulu11@gmail.com"
receiver = "luffynulu11@gmail.com"

def send_email(image_path):
    print("send email started")
    email_message = EmailMessage()
    email_message["Subject"] = "Some-one showed up!"
    email_message.set_content("There is a intruder")

    with open(image_path,"rb") as file:
        content = file.read()

    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None,content))
    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender,password)
    gmail.sendmail(sender, receiver, email_message.as_string())
    gmail.quit()
    print("send email ended")

if __name__ == "__main__":
    send_email()