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



## Demo Pictures
### This is front-end (Images are not uploaded)

<img width="1438" alt="1" src="https://github.com/user-attachments/assets/d3a8d81d-7d8c-4769-babc-265a0fd70ff8">

### This is front-end (After Images are uploaded But context is not provided)

<img width="1439" alt="2" src="https://github.com/user-attachments/assets/fa77bad4-79ef-4997-9818-c454d9b35058">

### All Images are
![1](https://github.com/user-attachments/assets/ad84a73b-de0c-4d3a-ba60-1726d1252b45)

![2](https://github.com/user-attachments/assets/1491cb93-3dd0-4643-b570-751e6d120978)

![3](https://github.com/user-attachments/assets/fcc3842d-b4f5-4c0b-8e13-af63d0d9825b)

![4](https://github.com/user-attachments/assets/8f475a26-d5ff-4b82-8bdb-ba09c881691a)

![5](https://github.com/user-attachments/assets/0573c55f-8077-4a19-bb33-bfa70af06a2f)

![6](https://github.com/user-attachments/assets/beb64b94-6620-4758-af73-74d44264bf94)

### Output from LLM

<img width="1437" alt="3" src="https://github.com/user-attachments/assets/084fed07-c07b-4247-9089-e1a659f442b3">

<img width="1436" alt="4" src="https://github.com/user-attachments/assets/05950c6b-d826-4bbd-b825-24382ede7253">

<img width="1440" alt="5" src="https://github.com/user-attachments/assets/f2c57ce6-380f-4bec-9eaa-ad6c675f28f8">


### This is front-end (After Images are uploaded And context is provided)

<img width="1436" alt="6" src="https://github.com/user-attachments/assets/c8c9c3a5-e6ee-47fe-8ca6-e8c697d79ef9">

### Output from LLM

<img width="1440" alt="7" src="https://github.com/user-attachments/assets/9183a45a-3903-4183-b396-047c16eb5ec9">

<img width="1440" alt="8" src="https://github.com/user-attachments/assets/8358e796-de50-4c0c-aa25-8a0f9cc5190e">

<img width="1440" alt="9" src="https://github.com/user-attachments/assets/45800f0b-b97f-4f5c-914d-275eb89bea57">

<img width="1440" alt="10" src="https://github.com/user-attachments/assets/d0d6926a-0be6-4f5e-ac9d-35245cf15d72">

