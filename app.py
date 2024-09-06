import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)


UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


api_key = os.getenv('GOOGLE_API_KEY')  


if not api_key:
    raise Exception("API key not found. Please set the GOOGLE_API_KEY environment variable.")


genai.configure(api_key=api_key)  


model = genai.GenerativeModel("gemini-1.5-flash")




def generate_test_cases(context, screenshots):
    test_cases = []
    screenshot_data = []

    NONE = "Give some more context or give some more images."


    for screenshot in screenshots:
        image = Image.open(screenshot)

        extracted_info = model.generate_content([context, image])
        screenshot_data.append(extracted_info.text.strip())  

    full_context = f"{context}" if context else "No specific context provided."



    prompt = f"""
    DOCUMENT:
    You are a QA expert reviewing the functionality of a digital product based on the following context and screenshots.

    Context: {full_context}

    Number of screenshots: {len(screenshot_data)}

    Screenshots' extracted information: {', '.join(screenshot_data)}

    QUESTION:
    How can the product's functionality be tested step-by-step?

    INSTRUCTIONS:
    - Answer the QUESTION using the DOCUMENT text above.
    - Generate a detailed, step-by-step guide for testing the digital product.
    - The guide should be structured into **Test Cases**, each containing:
        - **Description:** A general explanation of what the test case is about.
        - **Pre-conditions:** Any setup that needs to be done before performing the test.
        - **Testing Steps:** A sequence of steps for performing the test, avoiding specific values (like cities or dates).
        - **Expected Result:** What the expected outcome should be if the test passes.
    - Avoid using specific data such as names, cities, or dates in the testing steps.
    - Return the information in a general form based on the functionality, keeping the answer grounded in the provided DOCUMENT context and screenshots.
    """



    response = model.generate_content(prompt)
    instructions = response.text.strip()

    return instructions


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate-test-cases', methods=['POST'])
def generate_test_cases_route():
    context = request.form.get('context', '')


    screenshots = request.files.getlist('screenshots')


    instructions = generate_test_cases(context, screenshots)

    return jsonify({'instructions': instructions})

# Run the Flask app
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    app.run(debug=True)


    