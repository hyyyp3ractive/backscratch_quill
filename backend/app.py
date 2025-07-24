from flask import Flask, request, send_file, jsonify
from backend.docx_builder import build_mfr_docx
from backend.pdf_export import build_mfr_pdf
from backend.prompt_templates import build_prompt
import os
import openai

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/generate-docx", methods=["POST"])
def generate_docx():
    data = request.json
    output_path = build_mfr_docx(data)
    return send_file(output_path, as_attachment=True)

@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    data = request.json
    output_path = build_mfr_pdf(data)
    return send_file(output_path, as_attachment=True)

@app.route("/generate-ai", methods=["POST"])
def generate_ai_mfr():
    data = request.json
    prompt = build_prompt(data)

    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        ai_text = response["choices"][0]["message"]["content"]
        data["body"] = ai_text
        output_path = build_mfr_docx(data)
        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "<h1>Backscratch Quill – MFR Generator API is running.</h1><p>Use the frontend to submit a form and generate a .docx or .pdf.</p>"

if __name__ == "__main__":
    os.makedirs("exports", exist_ok=True)
    app.run(debug=True)
