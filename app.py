%%writefile app.py
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Tai Ahom Learning Platform", page_icon="🛕", layout="wide")

# Google Font (Noto Serif Ahom) আৰু ইফেক্টৰ বাবে CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+Ahom&display=swap');

.ahom-text {
    font-family: 'Noto Serif Ahom', serif !important;
    font-size: 50px !important;
    color: #FF5733;
    text-align: center;
    margin-bottom: 5px;
}
.phrase-text {
    font-family: 'Noto Serif Ahom', serif !important;
    font-size: 28px !important;
    color: #2E4053;
}
.card {
    border: 1px solid #ddd; 
    padding: 15px; 
    border-radius: 10px; 
    background-color: #f9f9f9; 
    text-align: center;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
}
.dict-result {
    font-family: 'Noto Serif Ahom', serif !important;
    font-size: 40px !important;
    color: #27AE60;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🛕 টাই আহোম ভাষা শিক্ষা কেন্দ্ৰ")
st.write("আহোম ভাষা সংৰক্ষণ, অভিধান আৰু ডিজিটেল প্ৰসাৰৰ এক প্ৰয়াস।")
st.markdown("---")

# Sidebar navigation
st.sidebar.title("মেনু (Menu)")
page = st.sidebar.radio("ক’লৈ যাব খোজে?", ["আখৰ পৰিচয় (Alphabets)", "শব্দকোষ/অভিধান (Dictionary)", "প্ৰয়োজনীয় বাক্য (Phrases)", "কুইজ খেল (Quiz Game)"])

# ----------------- SECTION 1: ALPHABETS -----------------
if page == "আখৰ পৰিচয় (Alphabets)":
    st.header("🔤 আহোম বৰ্ণমালা (Consonants)")
    
    alphabets = [
        {"Ahom": "𑜀", "Assamese": "ক (কা)", "English": "Ka"},
        {"Ahom": "𑜁", "Assamese": "খ (খা)", "English": "Kha"},
        {"Ahom": "𑜂", "Assamese": "ঙ (ঙা)", "English": "Nga"},
        {"Ahom": "𑜃", "Assamese": "ন (না)", "English": "Na"},
        {"Ahom": "𑜄", "Assamese": "ত (তা)", "English": "Ta"},
        {"Ahom": "𑜅", "Assamese": "থ (থা)", "English": "Tha"},
        {"Ahom": "𑜆", "Assamese": "প (পা)", "English": "Pa"},
        {"Ahom": "𑜇", "Assamese": "ফ (ফা)", "English": "Pha"},
        {"Ahom": "𑜈", "Assamese": "ব (বা)", "English": "Ba"},
        {"Ahom": "𑜉", "Assamese": "ম (মা)", "English": "Ma"},
        {"Ahom": "𑜊", "Assamese": "যা (জা)", "English": "Ja"},
        {"Ahom": "𑜋", "Assamese": "ছা (চা)", "English": "Cha"},
        {"Ahom": "𑜌", "Assamese": "ঞা (নিয়া)", "English": "Nya"},
        {"Ahom": "𑜍", "Assamese": "ৰ (ৰা)", "English": "Ra"},
        {"Ahom": "𑜎", "Assamese": "ল (লা)", "English": "La"},
        {"Ahom": "𑜏", "Assamese": "ছ (ছা/সা)", "English": "Sa"},
        {"Ahom": "𑜐", "Assamese": "হ (হা)", "English": "Ha"},
        {"Ahom": "𑜑", "Assamese": "অ (আ)", "English": "A"},
        {"Ahom": "𑜒", "Assamese": "খ্যা (খ্ৰা)", "English": "Khra"},
        {"Ahom": "𑜓", "Assamese": "ধ (ধা)", "English": "Dha"},
        {"Ahom": "𑜔", "Assamese": "নিয়া (ন্যা)", "English": "Nya"},
        {"Ahom": "𑜕", "Assamese": "দ্ৰ (দ্ৰা)", "English": "Dra"},
        {"Ahom": "𑜖", "Assamese": "ব্ৰ (ব্ৰা)", "English": "Bra"},
        {"Ahom": "𑜗", "Assamese": "প্ৰ (প্ৰা)", "English": "Pra"},
        {"Ahom": "𑜘", "Assamese": "ফ্ৰ (ফ্ৰা)", "English": "Phra"},
        {"Ahom": "𑜙", "Assamese": "গ (গা)", "English": "Ga"}
    ]
    
    cols = st.columns(4)
    for i, alpha in enumerate(alphabets):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card">
                <p class="ahom-text">{alpha['Ahom']}</p>
                <p style="margin:0; font-size:16px;"><b>উচ্চাৰণ:</b> {alpha['Assamese']}</p>
                <p style="margin:0; color:gray; font-size:14px;"><i>({alpha['English']})</i></p>
            </div>
            """, unsafe_allow_html=True)

# ----------------- SECTION 2: DICTIONARY -----------------
elif page == "শব্দকোষ/অভিধান (Dictionary)":
    st.header("🔍 স্মাৰ্ট টাই আহোম অভিধান (Search Dictionary)")
    st.write("অসমীয়া শব্দ টাইপ কৰি টাই আহোম অনুবাদ বিচাৰি উলিয়াওক:")
    
    # অভিধানৰ ডাটাবেচ
    dictionary = {
        "ধন্যবাদ": {"Ahom": "𑜋𑜡𑜥 𑜒𑜟𑜂𑜦 𑜃𑜩", "Pron": "চাও ব্লং নাই"},
        "মই": {"Ahom": "𑜁𑜿𑜡", "Pron": "খ্ৰু/খাও"},
        "ৰজা": {"Ahom": "𑜋𑜡𑜥", "Pron": "চাও"},
        "পানী": {"Ahom": "𑜃𑜪", "Pron": "নাম"},
        "ভাত": {"Ahom": "𑜁𑜡𑜥", "Pron": "খাও"},
        "ভাল": {"Ahom": "𑜃𑜦", "Pron": "নে"},
    }
    
    search_query = st.text_input("অসমীয়া শব্দ লিখক (যেনে: ধন্যবাদ, ৰজা, পানী, ভাত):").strip()
    
    if search_query:
        if search_query in dictionary:
            res = dictionary[search_query]
            st.success(f"🔍 '{search_query}' ৰ টাই আহোম ৰূপ পালেগৈ:")
            st.markdown(f"""
            <div style="background-color: #E8F8F5; padding: 20px; border-radius: 10px; border-left: 5px solid #27AE60;">
                <p style="margin:0; font-size:18px; color:#555;"><b>টাই আহোম লিপি:</b></p>
                <p class="dict-result">{res['Ahom']}</p>
                <p style="margin:5px 0 0 0; font-size:18px;"><b>উচ্চাৰণ:</b> {res['Pron']}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(" দুঃখিত! এই শব্দটো বৰ্তমান অভিধানত নাই। অতি সোনকালে যোগ কৰা হ’ব।")

# ----------------- SECTION 3: PHRASES -----------------
elif page == "প্ৰয়োজনীয় বাক্য (Phrases)":
    st.header("🗣️ দৈনন্দিন ব্যৱহৃত বাক্য (Common Phrases)")
    
    phrases = [
        {"Ahom": "𑜌𑜰𑜂𑜦𑜠 𑜏𑜣 𑜁𑜿𑜡 𑜃𑜦", "Assamese": "আপুনি কুশলে আছেনে? (ماو-মি-খ্ৰু-নে)", "English": "How are you?"},
        {"Ahom": "𑜁𑜿𑜡 𑜃𑜦", "Assamese": "মই ভালে আছোঁ। (খ্ৰু-নে)", "English": "I am fine."},
        {"Ahom": "𑜋𑜡𑜥 𑜒𑜟𑜂𑜦 𑜃𑜩", "Assamese": "ধন্যবাদ। (চাও ব্লং নাই)", "English": "Thank you."},
    ]
    
    st.markdown("""
    <style>
    table { width: 100%; border-collapse: collapse; }
    th, td { padding: 12px; border: 1px solid #ddd; text-align: left; }
    th { background-color: #f2f2f2; }
    </style>
    """, unsafe_allow_html=True)
    
    html_table = "<table><tr><th>টাই আহোম (Tai Ahom)</th><th>অসমীয়া অৰ্থ (Assamese)</th><th>English Meaning</th></tr>"
    for row in phrases:
        html_table += f"<tr><td><span class='phrase-text'>{row['Ahom']}</span></td><td>{row['Assamese']}</td><td><i>{row['English']}</i></td></tr>"
    html_table += "</table>"
    
    st.markdown(html_table, unsafe_allow_html=True)

# ----------------- SECTION 4: QUIZ -----------------
elif page == "কুইজ খেল (Quiz Game)":
    st.header("🧠 আপোনাৰ জ্ঞান পৰীক্ষা কৰক (Test Your Knowledge)")
    st.write("প্ৰশ্নসমূহৰ শুদ্ধ উত্তৰ বাছি উলিয়াওক:")
    
    score = 0
    
    # Question 1
    st.subheader("প্ৰশ্ন ১: 'ধন্যবাদ' বুজাবলৈ আহোমত কি বুলি কোৱা হয়?")
    q1 = st.radio("উত্তৰ ১:", ["ক) মাও-মি-খ্ৰু-নে?", "খ) চাও ব্লং নাই", "গ) খ্ৰু-নে"], index=None, key="q1")
    if q1 == "খ) চাও ব্লং নাই":
        score += 1

    st.markdown("---")
    # Question 2
    st.subheader("প্ৰশ্ন ২: আহোম ভাষাত 'পানী' ক কি বুলি কোৱা হয়?")
    q2 = st.radio("উত্তৰ ২:", ["ক) নাম (𑜃𑜪)", "খ) কা (𑜀)", "গ) চাও (𑜋𑜡𑜥)"], index=None, key="q2")
    if q2 == "ক) নাম (𑜃𑜪)":
        score += 1

    st.markdown("---")
    # Question 3
    st.subheader("প্ৰশ্ন ৩: ব্যঞ্জনবৰ্ণ '𑜀' ৰ অসমীয়া উচ্চাৰণ কি?")
    q3 = st.radio("উত্তৰ ৩:", ["ক) খা", "খ) ঙা", "গ) কা"], index=None, key="q3")
    if q3 == "গ) কা":
        score += 1
        
    st.markdown("---")
    if st.button("ফাইনাল ৰিজাল্ট চাওক"):
        st.balloons()
        st.metric(label="আপোনাৰ মোট স্ক’ৰ (Your Total Score)", value=f"{score} / 3")
        if score == 3:
            st.success("👑 অসাধাৰণ! আপুনি আটাইকেইটা প্ৰশ্নৰ শুদ্ধ উত্তৰ দিছে।")
        elif score > 0:
            st.info("ভাল প্ৰয়াস! অলপ অভ্যাস কৰিলে সকলো শুদ্ধ হ’ব।")
        else:
            st.error(" سفر! আকৌ এবাৰ আখৰ কেইটা ভালকৈ পঢ়ি চেষ্টা কৰক।")

st.markdown("---")
st.caption("Developed with ❤️ for Axom | Powered by Streamlit")