#!/usr/bin/env python3

from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    # attachment = "processed.pdf"
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)    
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    report.build([report_title, report_info])