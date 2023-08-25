import smtplib

# get user input for email details
sender_email = input("Enter your email address: ")
sender_password = input("Enter your email password: ")
recipient_email = input("Enter recipient email address: ")
subject = input("Enter email subject: ")
message = input("Enter email message: ")

# connect to the SMTP server
smtp_server = "smtp.gmail.com"  # for Gmail
port = 587  # for TLS
smtp_obj = smtplib.SMTP(smtp_server, port)
smtp_obj.starttls()
smtp_obj.login(sender_email, sender_password)

# create the email message
email_message = f"Subject: {subject}\n\n{message}"

# send the email
smtp_obj.sendmail(sender_email, recipient_email, email_message)

# disconnect from the SMTP server
smtp_obj.quit()

print("Email sent successfully!")
