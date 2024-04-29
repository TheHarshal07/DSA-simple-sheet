from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import re

app = Flask(__name__)

@app.route('/verify_pan', methods=['POST'])
def verify_pan():
    file = request.files['image']
    img = Image.open(file)
    extracted_text = pytesseract.image_to_string(img)
    
    name_pattern = re.compile(r'Name[^\w\n]*\n([^\n]+)', re.IGNORECASE)
    match = name_pattern.search(extracted_text)
    dob_pattern = re.compile(r'Date\s*of\s*Birth[^\d]*(\d{1,2}/\d{1,2}/\d{4})', re.IGNORECASE)
    dob_match = dob_pattern.search(extracted_text)

    if match:
        extracted_name = match.group(1).strip()
    else:
        extracted_name = "Name not found in the extracted text."

    if dob_match:
        extracted_dob = dob_match.group(1)
    else:
        extracted_dob = "Date of Birth not found in the text."

    return jsonify({'name': extracted_name, 'dob': extracted_dob})

if __name__ == '__main__':
    app.run(debug=True)