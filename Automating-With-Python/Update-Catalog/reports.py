#!/usr/bin/env python3

from datetime import datetime
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(title, additional_info):
    filename = "processed.pdf"
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)    
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])
    report.build([report_title, report_info])