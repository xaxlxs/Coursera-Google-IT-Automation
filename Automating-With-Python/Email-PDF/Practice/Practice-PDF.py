############################
# GENERATING A PDF DOCUMENT
############################

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

report = SimpleDocTemplate("/workspaces/Coursera-Google-IT-Automation/Automating-With-Python/Email-PDF/Practice/report.pdf")
styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# report.build([report_title])


#################
# ADDING A TABLE
#################

from reportlab.lib import colors

# Dictionary of data for table

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

# Turn data dictionary into a list of lists (array)

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

# print(table_data)

# Create the table

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# report.build([report_title, report_table])


#######################
# ADDING A PIE CHART
#######################

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.pagesizes import inch

report_pie = Pie(width=3*inch, height=3*inch)

report_pie.data = []
report_pie.labels = []
for name in sorted(fruit):
    report_pie.data.append(fruit[name])
    report_pie.labels.append(name)

# print(report_pie.data, "\n", report_pie.labels)

report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])