from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from jinja2 import Template
from src.utils.config import settings

# Criando a configuração com ConnectionConfig
conf = ConnectionConfig(
    MAIL_USERNAME=settings.SMTP_EMAIL,
    MAIL_PASSWORD=settings.SMTP_PASSWORD,
    MAIL_FROM=settings.SMTP_EMAIL,
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_SERVER=settings.SMTP_SERVER,
    MAIL_STARTTLS=True, 
    MAIL_SSL_TLS=False,  
)

# Passando a configuração corretamente para o FastMail
fm = FastMail(conf)

async def send_match_email(receiver_email: str, participant_name: str, match_name: str, group_name: str, group_date: str):
    with open("src/templates/email_template.html", "r", encoding="utf-8") as f:
        template = Template(f.read())

    html_content = template.render(
        participant_name=participant_name,
        match_name=match_name,
        group_name=group_name,
        group_date=group_date
    )

    message = MessageSchema(
        subject=f"Seu Amigo Secreto do grupo {group_name} 🎁", 
        recipients=[receiver_email],
        body=html_content,
        subtype="html",
    )

    await fm.send_message(message)
