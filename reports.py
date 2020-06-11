#!/usr/bin/env python3

from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file, title, add_info):
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(add_info, styles['BodyText'])
    report = SimpleDocTemplate(file)
    empty_line = Spacer(1,20)

    report.build([report_title, empty_line, report_info, empty_line])