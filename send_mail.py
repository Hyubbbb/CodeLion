import smtplib
from email.message import EmailMessage
import imghdr

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")

# Header
message["Subject"] = "이것은 제목입니다."
message["From"] = "ekwjsxl200@gmail.com"
message["To"] = "###@gmail.com"

with open("codelion.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('codelion',image_file) # 이미지 타입을 동적으로 할당
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) # (SSL)
smtp.login("ekwjsxl200@gmail.com","Wndus12345!@")
smtp.send_message(message)
smtp.quit()