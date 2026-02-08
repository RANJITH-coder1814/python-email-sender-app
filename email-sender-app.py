import smtplib
import ssl

def send_email():
    sender_email = input("Enter your email: ")
    receiver_email = input("Enter receiver email: ")
    password = input("Enter your email password / app password: ")
    subject = input("Enter subject: ")
    message = input("Enter message: ")

    text = f"Subject: {subject}\n\n{message}"

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            print("\n Email sent successfully!")

    except Exception as e:
        print("\n Error:", e)


if __name__ == "__main__":
    send_email()
