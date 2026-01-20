# ============================================
# AUTOMATED REPORT GENERATION USING REPORTLAB
# ============================================

import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

# --------------------------------------------
# STEP 1: CREATE / READ DATA FROM CSV FILE
# --------------------------------------------
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85, 90, 78, 92]
}

df = pd.DataFrame(data)

# Save data to CSV file
df.to_csv("sample_data.csv", index=False)

# --------------------------------------------
# STEP 2: ANALYZE THE DATA
# --------------------------------------------
average_score = df["Score"].mean()
highest_score = df["Score"].max()
lowest_score = df["Score"].min()

# --------------------------------------------
# STEP 3: GENERATE PDF REPORT
# --------------------------------------------
pdf = SimpleDocTemplate("report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# ---- Title ----
elements.append(Paragraph("Automated Report Generation", styles["Title"]))
elements.append(Spacer(1, 12))

# ---- Summary Section ----
elements.append(Paragraph("Summary Statistics", styles["Heading2"]))
elements.append(Paragraph(f"Average Score: {average_score:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Score: {highest_score}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Score: {lowest_score}", styles["Normal"]))
elements.append(Spacer(1, 12))

# ---- Detailed Data Table ----
elements.append(Paragraph("Detailed Data", styles["Heading2"]))

table_data = [df.columns.tolist()] + df.values.tolist()
table = Table(table_data)

table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("FONT", (0, 0), (-1, 0), "Helvetica-Bold")
]))

elements.append(table)

# ---- Build PDF ----
pdf.build(elements)

print("Report generated successfully!")
