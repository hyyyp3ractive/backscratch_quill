def build_prompt(data):
    return f"""
You are a military administrative assistant writing a Memorandum for Record (MFR) in accordance with the U.S. Air Force Tongue and Quill standard.

Use the following information to generate the body of the memorandum. Maintain professional tone, clarity, and concise formatting:

Recipient: {data.get('recipient', 'N/A')}
Subject: {data.get('subject', 'N/A')}
Purpose: {data.get('purpose', 'N/A')}
Justification: {data.get('justification', 'N/A')}
Requested Action: {data.get('action', 'N/A')}
Point of Contact: {data.get('poc', 'N/A')}

Format the body using appropriate paragraphing, starting with a Bottom Line Up Front (BLUF) sentence.
"""
from flask import Flask, request, send_file, jsonify
from backend.docx_builder import build_mfr_docx
from backend.pdf_export import build_mfr_pdf
from backend.prompt_templates import build_prompt
import os
import openai

app = Flask(__name__)

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
