############################
# GENERATING A PDF DOCUMENT
############################

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

report = SimpleDocTemplate("report.pdf")
styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

# report.build([report_title])


#################
# ADDING A TABLE
#################

from reportlab.lib import colors

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

# print(table_data)

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report.build([report_title, report_table])