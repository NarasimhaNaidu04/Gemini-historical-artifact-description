import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
from google import genai

# Load API key
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="Multimodal AI Blog Generator", layout="wide")

st.title("📝 Gemini Historical Artifact Description")

st.write("Provide a topic, an image, or both.")

# Inputs
topic = st.text_input("Enter Blog Topic (Optional):")
word_count = st.slider("Select Blog Length (Words)", 200, 2000, 800)

uploaded_image = st.file_uploader(
    "Upload an Image (Optional)",
    type=["jpg", "jpeg", "png"]
)

generate = st.button("Generate Blog")

if generate:

    if not topic and not uploaded_image:
        st.error("Please provide at least a topic or an image.")
    else:
        with st.spinner("Generating blog... ⏳"):

            try:
                base_prompt = f"""
                Generate a well-structured blog post.
                Target length: approximately {word_count} words.
                Include:
                - Catchy Title
                - Introduction
                - Subheadings
                - Conclusion
                """

                # CASE 1: Topic only
                if topic and not uploaded_image:
                    final_prompt = base_prompt + f"\nTopic: {topic}"

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=final_prompt
                    )

                # CASE 2: Image only
                elif uploaded_image and not topic:
                    image = Image.open(uploaded_image)

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[base_prompt + "\nAnalyze this image and write a blog.", image]
                    )

                # CASE 3: Both
                else:
                    image = Image.open(uploaded_image)

                    final_prompt = base_prompt + f"\nTopic: {topic}\nIncorporate the uploaded image."

                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[final_prompt, image]
                    )

                blog = response.text

                st.success("Blog Generated Successfully!")

                if uploaded_image:
                    st.image(uploaded_image, caption="Uploaded Image", width='stretch')

                edited_blog = st.text_area("Edit Blog (Optional):", blog, height=400)

                st.download_button(
                    label="Download Blog",
                    data=edited_blog,
                    file_name="generated_blog.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {e}")
