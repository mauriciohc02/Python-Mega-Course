from fpdf import FPDF
import pandas as pd


# Create a pdf instance with its configuration
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
# Read data from the .csv
df = pd.read_csv("db/topics.csv", sep=",")
# Iterate each row in the dataframe
for index, row in df.iterrows():
    topic = row["Topic"]
    num_pages = row["Pages"]
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(r=100, g=100, b=100)
    # Write each Topic in the PDF
    pdf.cell(w=0, h=12, txt=topic, align="L", ln=1)
    # Draw a lines under the Topic using coordinates
    for i in range(20, 298, 10):
        pdf.line(x1=10, y1=i, x2=200, y2=i)
    # Set the footer
    pdf.ln(265) # Breaklines from the title to the bottom
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(r=180, g=180, b=180)
    pdf.cell(w=0, h=10, txt=topic, align="R")
    # Add pages required for each Topic with its footer
    for _ in range(num_pages - 1):
        pdf.add_page()
        # Set the footer
        pdf.ln(277) # Breaklines from the top to the bottom
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(r=180, g=180, b=180)
        pdf.cell(w=0, h=10, txt=topic, align="R")
        # Draw a lines under the Topic using coordinates
        for i in range(20, 298, 10):
            pdf.line(x1=10, y1=i, x2=200, y2=i)


# Generate de PDF file
pdf.output("./files/output.pdf")
