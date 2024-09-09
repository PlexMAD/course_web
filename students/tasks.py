from celery import shared_task
from django.core.mail import send_mail
from .models import Projects


@shared_task
def send_email():
    projects = Projects.objects.all()

    email_body = "Список проектов и их даты окончания:\n\n"

    for project in projects:
        project_info = (
            f"Проект: {project.project_name}\nДата окончания: {project.end_date}\n\n"
        )
        email_body += project_info

    if email_body.strip():
        send_mail("Напоминание", email_body, "xd@gmail.com", ["xd@gmail.com"])
