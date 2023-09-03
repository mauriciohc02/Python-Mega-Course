import glob
from pathlib import Path
import pandas as pd
from fpdf import FPDF


# Get all .xlsx filenames into a list
filepaths = glob.glob(pathname="invoices/*.xlsx")

for filepath in filepaths:
    # Create a pdf instance with its configuration
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    # Get only the filename (no extension)
    filename = Path(filepath).stem
    # Get items from ["10001", "2023.1.18"]
    invoice_nr, date = filename.split("-")
    # Write Invoice Title
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)
    # Write Invoice Date
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)
    # Read data from the .xlsx
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Get headers from the dataframe
    columns = df.columns
    # Replace "_" to " " in each header and make it a Title
    columns = [item.replace("_", " ").title() for item in columns]
    # Add table's header
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(r=80, g=80, b=80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    # Create table's content (rows)
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(r=80, g=80, b=80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1) # Breakline

    # Sum all the values from the Total Price
    total_sum = df["total_price"].sum()
    # Add the last row for the Sum of Total Price
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(r=80, g=80, b=80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    # Add total sum sentence
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)
    # Add company name and logo
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=30, h=8, txt=f"PythonHow")
    pdf.image("./images/pythonhow.png", w=10)

    # Generate the PDF file
    pdf.output(f"PDFs/{filename}.pdf")
