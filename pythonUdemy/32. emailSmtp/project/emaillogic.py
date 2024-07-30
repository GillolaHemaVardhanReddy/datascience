import smtplib

def sendmail(**kargs):
    # myemail = "gillolahemavardhanreddy@gmail.com"
    passcode = "fgrw ogxw izif tnec"  # Use the generated app password here
    # tomail = "balabittu1143@gmail.com"
    myemail = kargs.get("frm")
    tomail = kargs.get("to")

    try:
        # Create a new smtp object named connection because it is used to connect our email providers
        # connection = smtplib.SMTP("smtp.gmail.com", 587)  # include the port number
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            # tls transport layer security is a way to securing our connection
            connection.starttls() 

            # login details
            connection.login(user=myemail, password=passcode)

            # Constructing the email
            # subject = "Subject: Test Email\n"
            # body = "Hello, this is a test email."
            msg = kargs.get("subject") + "\n" + kargs.get("body")

            # Sending email
            connection.sendmail(from_addr=myemail, to_addrs=tomail, msg=msg)

    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
        print("Please check your email and password, or consider using an app password if you have 2-Step Verification enabled.")

    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Email sent successfully!")
    # finally:
        # Close the connection
        # connection.quit()

