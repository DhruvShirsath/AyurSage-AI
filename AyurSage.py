import streamlit as st
import requests
import json
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv  # Import the load_dotenv function
import os  # Import the os module to access environment variables

# Load environment variables from .env file
load_dotenv()

# Set your Groq API key and model name
api_key = os.getenv("GROQ_API_KEY")  # Load the API key from .env
if not api_key:
    st.error("GROQ_API_KEY not found in .env file. Please add it and restart the app.")
    st.stop()  # Stop the app if the API key is missing

# Set your Groq API key and model name
model_name = "llama-3.3-70b-versatile"
groq_api_url = "https://api.groq.com/openai/v1/chat/completions"  # Correct endpoint for Groq API

# Define a prompt template for Ayurvedic recommendations
prompt_template = PromptTemplate(
    input_variables=["symptoms", "disease"],
    template="""
    You are an experienced Ayurvedic doctor with deep knowledge of traditional Indian medicine. Based on the following symptoms and disease (if provided), provide:
    1. Possible diseases or conditions.
    2. Ayurvedic medicines or remedies.
    3. Lifestyle and dietary recommendations.
    4. Things to avoid.

    Symptoms: {symptoms}
    Disease (optional): {disease}

    Response Format:
    - Possible Diseases: <list of diseases>
    - Ayurvedic Medicines: <list of medicines>
    - Lifestyle Recommendations: <list of recommendations>
    - Things to Avoid: <list of things to avoid>

    Example:
    Symptoms: fever, cough, and body ache
    Disease: Common cold
    - Possible Diseases: Common cold, flu, or viral fever.
    - Ayurvedic Medicines:
      1. Tulsi (Holy Basil) tea to reduce fever and cough.
      2. Ginger and honey mixture for sore throat.
      3. Turmeric milk to boost immunity.
    - Lifestyle Recommendations:
      1. Rest and stay hydrated.
      2. Avoid cold and oily foods.
      3. Practice steam inhalation with eucalyptus oil.
    - Things to Avoid:
      1. Cold drinks and ice cream.
      2. Oily and fried foods.
      3. Exposure to cold wind.
    """
)

# Function to generate response using Groq API
def generate_response(symptoms, disease=""):
    prompt = prompt_template.format(symptoms=symptoms, disease=disease)
    
    # Prepare the payload for Groq API
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 300,  # Adjust as needed
        "temperature": 0.7,  # Adjust for creativity
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    
    # Make the API request
    response = requests.post(groq_api_url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Groq API Error: {response.status_code} - {response.text}")

# Function to format the model's response
def format_response(response):
    # Remove unnecessary text like "Symptoms: fever Disease:"
    response = response.replace("Symptoms: fever Disease:", "").strip()
    
    # Split the response into sections
    sections = {
        "Possible Diseases": "",
        "Ayurvedic Medicines": "",
        "Lifestyle Recommendations": "",
        "Things to Avoid": ""
    }
    
    # Extract each section
    for section in sections:
        if section in response:
            start = response.find(section) + len(section) + 1  # +1 to skip the colon
            end = response.find("Ayurvedic Medicines:") if section == "Possible Diseases" else \
                  response.find("Lifestyle Recommendations:") if section == "Ayurvedic Medicines" else \
                  response.find("Things to Avoid:") if section == "Lifestyle Recommendations" else \
                  len(response)
            sections[section] = response[start:end].strip()
    
    return sections

# Function to display the formatted response
def display_response(sections):
    for section, content in sections.items():
        if content:
            st.markdown(f'<p class="subheading">{section}</p>', unsafe_allow_html=True)
            # Split content into points and display with colorful arrows
            points = content.split("\n")
            for point in points:
                if point.strip():
                    st.markdown(f'<p class="point"> {point.strip()}</p>', unsafe_allow_html=True)

# Streamlit App
st.set_page_config(page_title="AyurSage", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
        * {
            font-family: 'Times New Roman', serif !important;
        }
    </style>
""", unsafe_allow_html=True)

# Custom CSS for styling
st.markdown("""
    <style>
        .title {
            font-size: 48px !important;
            font-weight: bold !important;
            color: #2E86C1 !important;
            text-align: center;
        }
        .subheading {
            font-size: 28px !important;
            font-weight: bold !important;
            color: #808000 !important;
            margin-top: 20px;
        }
        .point {
            font-size: 18px !important;
            
            margin-left: 20px;
        }
        .sidebar .sidebar-content {
            background-color: #F4F6F6;
            padding: 20px;
            border-radius: 10px;
        }
        .disclaimer {
            font-size: 16px !important;
            font-weight: bold !important;
            color: #E74C3C !important;
        }
        .sidebar-title {
            font-size: 30px !important;
            font-weight: bold !important;
            color: #FFCE1B !important;
            text-align: center;
            margin-bottom: 20px;
        }
        .sidebar-subtitle {
            font-size: 24px !important;
            font-weight: bold !important;
            color: #FF0000 !important;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .sidebar-text {
            text-align: justify;
            line-height: 1.6;
            font-size: 18px;
            
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar with project information and disclaimer
with st.sidebar:
    # About This Project section
    st.markdown('<p class="sidebar-title">About This Project</p>', unsafe_allow_html=True)
    st.markdown("""
        <p class="sidebar-text">
            This AI-powered app provides Ayurvedic recommendations based on symptoms and optional disease names. 
            It uses advanced language models to generate suggestions for:
            <ul class="sidebar-text">
                <li>Possible diseases</li>
                <li>Ayurvedic medicines</li>
                <li>Lifestyle recommendations</li>
                <li>Things to avoid</li>
            </ul>
        </p>
    """, unsafe_allow_html=True)

    # Disclaimer section
    st.markdown('<p class="sidebar-subtitle">Disclaimer</p>', unsafe_allow_html=True)
    st.markdown("""
        <p class="sidebar-text">
            ⚠️ This app provides AI-generated recommendations and is not a substitute for professional medical advice. Always consult a certified doctor for accurate diagnosis and treatment.
        </p>
    """, unsafe_allow_html=True)

# Main content
st.markdown('<p class="title">🌿 AyurSage - Nature’s Healing, Enhanced by AI 🌿</p>', unsafe_allow_html=True)
st.markdown("""
    <p style="text-align: center; font-size: 20px; color: #5D6D7E;">
        Enter your symptoms and (optionally) a disease name to get Ayurvedic recommendations.
    </p>
""", unsafe_allow_html=True)



# Input fields
symptoms = st.text_area("### Enter your symptoms (e.g., fever, cough, body ache):", height=100)
disease = st.text_input("Enter a disease name (optional):")

# Generate button
if st.button("Get Recommendations"):
    if symptoms.strip() == "":
        st.error("Please enter at least one symptom.")
    else:
        with st.spinner("Generating recommendations..."):
            try:
                response = generate_response(symptoms, disease)
                sections = format_response(response)
                st.success("Here are your Ayurvedic recommendations:")
                display_response(sections)
            except Exception as e:
                st.error(f"An error occurred: {e}")