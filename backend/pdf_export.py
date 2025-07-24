import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

def build_mfr_pdf(data):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("mfr_template.html")
    html_out = template.render(data)

    output_path = os.path.join("exports", "output_mfr.pdf")
    pdfkit.from_string(html_out, output_path)
    return output_path
