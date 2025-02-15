import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech

# Load pre-trained models for landmark recognition and description generation
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def recognize_landmark(image):
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    landmark_name = processor.decode(out[0], skip_special_tokens=True)
    return landmark_name

def support_multilingual(text, target_language):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def handle_accessibility(description, accessibility_option):
    if accessibility_option == "audio":
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text=description)
        voice = texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
        
        with open("output.mp3", "wb") as out:
            out.write(response.audio_content)
            return "Audio description saved as output.mp3"
    return description

st.title("Gemini Landmark Description App")
st.write("Enhance your tourist experiences by getting detailed information about iconic landmarks.")

uploaded_file = st.file_uploader("Upload an image of the landmark", type=["jpg", "jpeg", "png"])
user_prompt = st.text_input("Enter a brief prompt (e.g., 'Tell me about the history and architecture.')")
language = st.selectbox("Select language", ["en", "es", "fr", "de", "it"])
accessibility_option = st.selectbox("Select accessibility option", ["none", "audio"])

if st.button("Get Description"):
    if uploaded_file is not None and user_prompt:
        image = Image.open(uploaded_file)
        landmark_name = recognize_landmark(image)
        description = f"Landmark: {landmark_name}. {user_prompt}"
        description = support_multilingual(description, language)
        description = handle_accessibility(description, accessibility_option)
        
        st.write(description)
        
        if accessibility_option == "audio":
            audio_file = open("output.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
    else:
        st.write("Please upload an image and enter a prompt.")