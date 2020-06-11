#!/usr/bin/env python3
import email
import smtplib
import os
import mimetypes


def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message_body = email.message.EmailMessage()
    message_body["From"] = sender
    message_body["To"] = recipient
    message_body["Subject"] = subject
    message_body.set_content(body)

    # Making attachment_path optional, if the attachment variable is empty string, no email will be sent.
    if not attachment_path == "":
        # Process the attachment and add it to the email
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            message_body.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype,
                                   filename=attachment_filename)

    return message_body

def send_email(message_body):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message_body)
    mail_server.quit()
