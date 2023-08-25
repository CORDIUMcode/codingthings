import smtplib

sender_email = input("Enter your email address: ")
sender_password = input("What is your email password: ")
recipients_email = input("Enter recipient emails: ") 
subject = input("Enter email subject: ")
message = input("Enter email message: ")

smtp_server = "smtp.gmail.com"
port = 587
smtp_obj = smtplib.SMTP(smtp_server, port)
smtp_obj.starttls()
smtp_obj.login(sender_email, sender_password)

email_message = f"Subject: {subject}\n\n{message}"

smtp_obj.sendmail(sender_email, recipients_email, email_message)

smtp_obj.quit()

print("Email sent successfully! ")
