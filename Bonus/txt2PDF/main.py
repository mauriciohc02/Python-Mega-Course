from pathlib import Path
import glob
from fpdf import FPDF


# Get all .txt filenames into a list
filepaths = glob.glob("./files/*.txt")
# Create a pdf instance with its configuration
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    # Get only the filename (no extension)
    filename = Path(filepath).stem
    # Convert to Title the filename
    name = filename.title()
    # Add the name to the PDF as the title
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)
    # Get the content of each .txt
    with open(filepath, "r") as file:
        content = file.read()
    # Add the .txt content to the PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

# Generate the PDF file
pdf.output("./PDFs/output.pdf")
