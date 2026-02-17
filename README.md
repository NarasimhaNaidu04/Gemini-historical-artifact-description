**Gemini historical artifact description**
Powered by Streamlit & Gemini 2.5 Flash
An AI-powered web application that generates well-structured, engaging blog posts using Google Gemini 2.5 Flash.

The app supports:

✅ Text-based blog generation

✅ Image-based blog generation

✅ Multimodal (Text + Image) input

✅ Custom word count

✅ Editable output

✅ Download generated blog

🚀 Features
🔹 Generate blogs from a topic prompt

🔹 Upload an image to generate contextual blog content

🔹 Combine topic + image for richer output

🔹 Adjustable word count (200–2000 words)

🔹 Clean and responsive Streamlit UI

🔹 Secure API key handling using .env

🔹 Download generated blog as .txt

🛠 Tech Stack
Python

Streamlit

Google Gemini 2.5 Flash (google-genai SDK)

Pillow (Image Processing)

python-dotenv (Environment Variables)

🧠 How It Works
User provides:

Blog topic (optional)

Image (optional)

Desired word count

The app:

Constructs a structured prompt

Sends request to Gemini 2.5 Flash

Generates well-formatted blog content

Output:

Displays blog in editable format

Allows user to download content

📂 Project Structure
ai-blog-generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env   (Not uploaded to GitHub)
🔐 Environment Setup
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/ai-blog-generator.git
cd ai-blog-generator
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add API Key
Create a .env file in the root folder:

GEMINI_API_KEY=your_api_key_here
⚠️ Do NOT upload .env to GitHub.

5️⃣ Run the Application
streamlit run app.py
Open browser:

http://localhost:8501
📸 Example Use Cases
AI content creation

Blog automation

Academic article drafting

Marketing content generation

Image-based storytelling

🎯 Key Concepts Implemented
Reactive UI using Streamlit

Multimodal AI integration

Session state management

Controlled API execution

Environment-based secret management

🚀 Future Improvements
User authentication

Blog history storage (Database)

PDF export feature

SEO optimization mode

Cloud deployment (AWS / Streamlit Cloud)

Multi-user support
