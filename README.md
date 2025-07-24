# backscratch_quill

## Overview

This project is a web-based MFR generator designed to assist U.S. Air Force personnel in drafting **Tongue & Quill-compliant** memorandums using AI. Hosted externally on **Replit**, it acts as a companion to the Microsoft 365-based **Operations Master Suite** where sensitive content is finalized and stored.

Due to government restrictions on AI use within NIPRNet, this tool allows for **secure, external draft generation** via OpenAI or Claude API integrations. It also provides a fallback offline template generator for zero-AI environments.

---

## Features

### Form-Based Frontend

* Input fields for recipient, subject, justification, POC, suspense, etc.
* AI-assisted draft toggle (or manual formatting only)
* Preview/edit section
* Export as `.docx` or `.pdf`

### AI Backend

* Claude or OpenAI API integration
* Structured prompts to match Tongue & Quill standards
* Secure disclaimer warning for DoD/FOUO content

### Compliance Mode

* Prominent disclaimers: "Do not input CUI or PII"
* All data stays client-side unless sent to external API (clearly disclosed)

### Templates (Optional)

* Commander, DO, SNCOIC, or unit-specific MFR presets
* Prompts optimized for formal tone and mission-alignment
* Appointment letters and forms with tables, training blocks, and signature fields

### Offline Template Generator (Zero-AI)

* Create a blank MFR template using a local `.docx` generator
* Includes editable placeholders for date, subject, body, and contact info
* Optional table blocks for lists, appointment letters, or verification forms

### PDF Digital Signature Block Support

* Option to include signatory section in `.pdf` export
* Placeholder for digital signature fields
* Support for common PDF tools to apply CAC-enabled or typed digital signatures

---

## File Structure

```text
mfr-generator/
├── backend/
│   └── app.py             # Flask or FastAPI backend
├── frontend/
│   ├── index.html         # Form UI
│   ├── style.css          # Basic layout
│   └── script.js          # API calls + DOM logic
├── prompts/
│   └── sample_prompt.md   # Claude/OpenAI prompt examples
├── exports/
│   └── output_sample.docx # Example output MFR
├── templates/
│   └── blank_template.docx # Offline MFR fallback
├── README.md              # Project overview & setup
└── requirements.txt       # Dependencies
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mfr-generator.git
cd mfr-generator
```

### 2. Setup Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add API Key

Set your Claude or OpenAI key as an environment variable:

```bash
export OPENAI_API_KEY=your-key-here
```

### 4. Run the App

```bash
python backend/app.py
```

Visit `http://localhost:5000` to use the tool.

---

## Sample Prompt for AI

```text
You are a military administrative assistant writing a memorandum for record in compliance with the U.S. Air Force Tongue and Quill standard. Based on the following input, generate a complete MFR:

- Recipient: Capt Jordan Lee
- Subject: Emergency Response Training
- Purpose: To document A1C Vega's completion of ER training on 15 July
- Justification: Required for readiness compliance and squadron reporting
- Requested Action: None
- Point of Contact: TSgt Ramos, DSN 555-1234
```

---

## License

MIT License

---

## Future Plans

* Login/save feature via Firebase or Replit DB
* `.docx` export with dynamic headers
* Workflow checklist for routing approvals
* Template editor
* Air Force form fill automation (AF Form 1768, etc.)
* Drag/drop offline MFR builder using `python-docx`
* PDF signature support using `reportlab` or `PyPDF2`

---

## Contributing

Want to help build better tools for Airmen? PRs and forks are welcome. Please reach out or open an issue with ideas, bugs, or integrations.

---

## Disclaimer

> This tool is intended for unclassified use only. Do not input PII, CUI, or FOUO data into the AI prompt fields. Final versions of all MFRs must be reviewed and routed through official DoD channels.
