from agents import Agent, function_tool
import os
import sendgrid
from sendgrid.helpers.mail import To, Email, Mail, Content

INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

@function_tool
def send_email(subject: str, html_body: str) -> str:
    """ Send out an email with the given subject and HTML body to all sales prospects """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("kaya.atsy@gmail.com")
    to_email = To("kaya.atsy@gmail.com")
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    sg.client.mail.send.post(request_body=mail) # type: ignore
    return "Successfully sent email"

email_agent = Agent(
    name="Email Agent",
    model="gpt-4o-mini",
    instructions=INSTRUCTIONS,
    tools=[send_email]
)