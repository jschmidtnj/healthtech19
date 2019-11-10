# pip install fpdf
from fpdf import FPDF
from Update_Body import *
from generategraphs import *
import os

def export(name="Marco Polimeni", medications=[]):
	pdf = FPDF(orientation="P", unit="mm", format="letter")

	pdf.add_page()

	pdf.set_font("Arial", "B", size=20)
	pdf.cell(w=0, h=5, txt="Report for %s" % name, align="C")
	pdf.set_font("Arial", size=12)

	# Line Graph
	lineplot()
	pdf.image("output.png", 10, 50, 75, 75)
	os.remove("output.png")

	# Body Map
	update()
	pdf.image("humanOut.png", 100, 50, 95, 200)
	os.remove("humanOut.png")

	pdf.add_page()

	pdf.set_font("Arial", "B", size=20)
	pdf.cell(w=0, h=5, txt="Report for %s" % name, align="C", ln=1)
	pdf.set_font("Arial", "I", size=18)
	pdf.cell(w=0, h=35, txt="Medications", ln=1)
	pdf.set_font("Arial", size=12)

	height = 36
	for med in medications:
		pdf.cell(w=0, h=height, txt="   - "+med, ln=1)
		height += 1

	pdf.output("testing.pdf", 'S')
if __name__ == '__main__':
	export("Rocco Polimeni", ["Epipen", "Advil", "Acetominophen"])