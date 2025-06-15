from fastapi import FastAPI, BackgroundTasks, APIRouter
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from typing import List

router = APIRouter(prefix="/emails", tags=["emails"])

email_conf = ConnectionConfig(
    MAIL_USERNAME="your_email@example.com",
    MAIL_PASSWORD="your_password",
    MAIL_FROM="your_email@example.com",
    MAIL_PORT=587,  # 通常587用于STARTTLS，465用于SSL
    MAIL_SERVER="smtp.example.com",
    MAIL_STARTTLS=True,  # 明确设置STARTTLS
    MAIL_SSL_TLS=False,  # 明确设置SSL/TLS
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


class EmailSchema(BaseModel):
    email: List[EmailStr]
    body: str


@router.post("/send-email-background/")
async def send_in_background(background_tasks: BackgroundTasks, email_data: EmailSchema):
    message = MessageSchema(
        subject="FastAPI Mail",
        recipients=email_data.email,
        body=email_data.body,
        subtype="html"
    )
    fm = FastMail(email_conf)
    background_tasks.add_task(fm.send_message, message)

    return {"message": "Email has been sent in background"}
