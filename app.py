import streamlit as st
import google.generativeai as genai

# --- PAGE CONFIGURATION ---
st.set_title = "Tai Ahom Learning Platform with AI"
st.set_page_config(page_title="Tai Ahom Learning Platform", page_icon="🛕", layout="wide")

# --- GEMINI AI SETUP ---
# ইয়াত আপোনাৰ আচল API Key টো বহুবাব লাগিব
# সুৰক্ষাৰ বাবে আমি ইয়াক streamlit secrets ত ৰাখিব পাৰোঁ, এতিয়াৰ বাবে ডাইৰেক্ট চেক কৰিবলৈ দিছোঁ
API_KEY = "AIzaSyA6D895wPbpD69FEaV8AfMKcR7YvadVxks" 

if API_KEY != "আপোনাৰ_GEMINI_API_KEY_ইয়াত_পেষ্ট_কৰক":
    genai.configure(api_key=API_KEY)
else:
    st.error("অনুগ্ৰহ কৰি কোডৰ ভিতৰত আপোনাৰ আচল Gemini API Key টো বহুবাই লওক!")

# --- GOOGLE FONT (Noto Serif Ahom) & CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Ahom&display=swap');
.ahom-text {
    font-family: 'Noto Serif Ahom', serif !important;
    font-size: 45px !important;
    color: #FF5733;
    text-align: center;
}
.title-text {
    text-align: center;
    color: #4A154B;
    font-weight: bold;
}
</style>
""", unsafe_with_html=True)

# --- SIDEBAR MENU ---
st.sidebar.title("মেনু (Menu)")
choice = st.sidebar.radio("ক’লৈ যাব খোজে?", [
    "🛕 টাই আহোম এআই দোভাষী (AI Translator)",
    "🔤 আখৰ পৰিচয় (Alphabets)",
    "📚 শব্দকোষ (Dictionary)"
])

# --- SYSTEM PROMPT FOR AI ---
# এই প্ৰম্পটটোৱে এআইক বুজাব যে সি কেনেকৈ উত্তৰ দিব লাগিব
SYSTEM_INSTRUCTION = """
You are 'AxomAI Tai-Ahom Translator', an expert in Tai-Ahom language, script, and culture. 
Your job is to help users learn Tai-Ahom. When a user asks a question in Assamese or English, 
you must translate it into Tai-Ahom, explain the pronunciation, and provide cultural context if needed.
Always be polite and helpful. Speak primarily in Assamese when explaining to the user.
"""

# --- OPTION 1: AI TRANSLATOR ---
if choice == "🛕 টাই আহোম এআই দোভাষী (AI Translator)":
    st.markdown("<h1 class='title-text'>🛕 টাই আহোম এআই দোভাষী</h1>", unsafe_with_html=True)
    st.write("অসমীয়া বা ইংৰাজীত যিকোনো বাক্য লিখক, আমাৰ AI-এ তাক টাই আহোম ভাষালৈ অনুবাদ কৰি বুজাই দিব!")
    
    # User input input box
    user_query = st.text_input("আপুনি কি জানিব খোজে ইয়াতে টাইপ কৰক:", placeholder="যেনে: মই ভাত খালোঁ ইয়াক কি বুলি ক’ব?")
    
    if st.button("অনুবাদ কৰক (Translate)"):
        if user_query:
            with st.spinner("আমাৰ AI দোভাষীয়ে চিন্তা কৰি আছে..."):
                try:
                    # Calling Gemini Model
                    model = genai.GenerativeModel(
                        model_name="gemini-1.5-flash",
                        system_instruction=SYSTEM_INSTRUCTION
                    )
                    response = model.generate_content(user_query)
                    
                    # Display response
                    st.success("উত্তৰ সাজু:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"এৰৰ আহিছে কাকু! হয়তো API Key টো ভুল হৈছে। সবিশেষ: {e}")
        else:
            st.warning("অনুগ্ৰহ কৰি কিবা এটা টাইপ কৰক!")

# --- OPTION 2: ALPHABETS ---
elif choice == "🔤 আখৰ পৰিচয় (Alphabets)":
    st.markdown("<h1 class='title-text'>🔤 আহোম বৰ্ণমালা (Consonants)</h1>", unsafe_with_html=True)
    
    # সৰু ডাটাবেচ
    letters = [
        {"char": "𑜒", "name": "ক (Ka)"},
        {"char": "𑜓", "name": "খ (Kha)"},
        {"char": "𑜕", "name": "ঙ (Nga)"},
        {"char": "𑜗", "name": "চ (Ca)"}
    ]
    
    cols = st.columns(4)
    for i, let in enumerate(letters):
        with cols[i]:
            st.markdown(f"<p class='ahom-text'>{let['char']}</p>", unsafe_with_html=True)
            st.markdown(f"<p style='text-align:center;'><b>উচ্চাৰণ:</b> {let['name']}</p>", unsafe_with_html=True)

# --- OPTION 3: DICTIONARY ---
elif choice == "📚 শব্দকোষ (Dictionary)":
    st.markdown("<h1 class='title-text'>📚 বুৰঞ্জীমূলক শব্দকোষ</h1>", unsafe_with_html=True)
    st.write("কিছুমান প্ৰয়োজনীয় টাই আহোম শব্দৰ অৰ্থ:")
    
    words = {
        "ফাই (Phrang)": "জুই / অগ্নি",
        "নাম (Nam)": "পানী / নদী",
        "খুন (Khun)": "ৰজা / শাসনকৰ্তা",
        "লুং (Lung)": "ডাঙৰ / প্রধান"
    }
    
    for k, v in words.items():
        st.info(f"**{k}** ➡️  {v}")
