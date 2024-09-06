# Multimodal LLM Testing Instructions Generator Tool

## Overview
This project is a Testing Instructions Generator Tool that utilizes a multimodal Large Language Model (LLM) to describe detailed testing instructions for any digital product's features based on screenshots and optional context. It provides step-by-step test cases including descriptions, pre-conditions, steps, and expected results.

## Features
### Front-end:
- **Text Box for Optional Context:** Allows users to input context or specific requirements for the testing instructions.
- **Multi-image Uploader:** Users can upload one or more screenshots of the digital product.
- **Describe Testing Instructions Button:** Upon clicking, the tool generates the testing instructions based on the screenshots and optional context.

### Back-end:
- **Multimodal LLM Integration:** Processes the screenshots and context to generate a detailed step-by-step guide on how to test each feature.
- Each generated test case includes:
    - **Description:** A summary of what the test case is about.
    - **Pre-conditions:** Requirements that need to be met before testing.
    - **Testing Steps:** Clear, step-by-step instructions for the testing process.
    - **Expected Result:** What the user should observe if the feature is functioning correctly.

## Technologies Used
- **Flask (Python):** For building the back-end web server.
- **HTML/CSS/JavaScript:** For building the front-end interface.
- **Multimodal LLM (e.g., Gemini 1.5 Flash):** For processing images and generating textual test instructions.
- **PIL (Python Imaging Library):** To handle image uploads and conversion.
- **Bootstrap:** For responsive front-end design.

## Installation & Setup
### Prerequisites
- Python 3.9+
- Virtual Environment (recommended)

### Steps
1. Clone the Repository
```
git clone <repository-url>
cd llm
```
2. Create a Virtual Environment (optional but recommended)
```
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate      # For Windows
```
3. Install Dependencies Install the required Python packages listed in the `requirements.txt`:
```
pip install -r requirements.txt
```
4. Set Up Your API Key
- Create `.env` file and add Google Api like below
```
GOOGLE_API_KEY = 'your-gemini-api-key'  # Replace with your actual API key
```
5. Run the Application
```
python app.py
```

> The app will be available at `http://localhost:5000`.

![Uploading 1.png…]()
