import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Step 1: Generate a 6-digit random number
otp = str(random.randint(100000, 999999))

# Step 2: Store the OTP in a variable (you can store it in a database for verification)
# For this example, we'll store it in a dictionary
otp_storage = {}

# Step 3: Configure email settings
sender_email = 'ishaqbhai327@gmail.com'
app_password = 'uvea smrw jczh ewvk'  # Use the App Password you generated
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Step 4: Send OTP via email
def send_email(receiver_email, otp):
    subject = 'Your OTP Verification Code'
    message = f'Your OTP code is: {otp}'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, app_password)  # Use the App Password here
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print('OTP sent successfully!')
    except Exception as e:
        print(f'Error sending OTP: {str(e)}')

# Step 5: Request user input
user_email = input('Enter your email: ')

# Store the OTP in a dictionary before sending the email
otp_storage[user_email] = otp

send_email(user_email, otp)

user_input_otp = input('Enter the OTP sent to your email: ')

# Verify the OTP
if otp_storage.get(user_email) == user_input_otp:
    print('OTP verification successful!')
else:
    print('OTP verification failed!')
