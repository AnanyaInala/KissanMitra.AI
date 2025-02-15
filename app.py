import os
from PIL import Image
import torch
from torchvision import transforms
from transformers import BlipProcessor, BlipForConditionalGeneration
import google.generativeai as genai
import streamlit as st
import wikipedia
from difflib import get_close_matches

# Set up Gemini API Key (Replace with your actual key)
GOOGLE_GEMINI_API_KEY = "AIzaSyDBfG-fFPxipeebIJFJijBrHOKr13S9rrU"

genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

# Load pre-trained Hugging Face BLIP model for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Define image preprocessing
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# List of famous Indian landmarks
INDIAN_LANDMARKS = [
    "Taj Mahal", "Qutub Minar", "Gateway of India", "India Gate", "Mysore Palace",
    "Hawa Mahal", "Red Fort", "Charminar", "Lotus Temple", "Victoria Memorial",
    "Ajanta Caves", "Meenakshi Temple", "Golden Temple", "Sanchi Stupa",
    "Ellora Caves", "Brihadeeswarar Temple", "Sun Temple, Konark", "Humayun's Tomb",
    "Amber Fort", "Jantar Mantar", "Mahabalipuram", "Elephanta Caves", "Golconda Fort",
    "Rashtrapati Bhavan", "Rani Ki Vav", "Chittorgarh Fort", "Jagannath Temple, Puri"
]

def clean_landmark_name(landmark_name):
    """Fix incorrect landmark names using fuzzy matching."""
    match = get_close_matches(landmark_name, INDIAN_LANDMARKS, n=1, cutoff=0.4)
    return match[0] if match else landmark_name  # Use closest match if found

def recognize_landmark(image):
    """Recognize the landmark in the image using Hugging Face BLIP model."""
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    landmark_name = processor.decode(out[0], skip_special_tokens=True)
    return clean_landmark_name(landmark_name)  # Apply correction

def get_historical_info(landmark_name):
    """Fetch historical information about the landmark from Wikipedia."""
    corrected_name = clean_landmark_name(landmark_name)
    try:
        return wikipedia.summary(corrected_name, sentences=5)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple entries found for {corrected_name}: {e.options}"
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for {corrected_name}."

def generate_detailed_description(landmark_name, history_info, user_prompt):
    """Use Gemini AI to generate a rich description."""
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Describe the {landmark_name}. {user_prompt}. Here is some historical information: {history_info}"
    response = model.generate_content(prompt)
    return response.text.strip() if response else "Could not generate a detailed description."

# Streamlit UI
st.title("Gemini Landmark Description App")
st.write("Get AI-powered descriptions and historical insights on famous  landmarks.")

uploaded_file = st.file_uploader("Upload an image of an landmark", type=["jpg", "jpeg", "png"])
user_prompt = st.text_input("Enter a brief prompt (e.g., 'Tell me about the history and significance.')")

if st.button("Get Description"):
    if uploaded_file is not None and user_prompt:
        image = Image.open(uploaded_file)
        landmark_name = recognize_landmark(image)
        historical_info = get_historical_info(landmark_name)
        detailed_description = generate_detailed_description(landmark_name, historical_info, user_prompt)

        st.write(f"**Landmark:** {landmark_name}")
        st.write(f"**Historical Information:** {historical_info}")
        st.write(f"**AI-Generated Description:** {detailed_description}")
    else:
        st.write("Please upload an image and enter a prompt.")
