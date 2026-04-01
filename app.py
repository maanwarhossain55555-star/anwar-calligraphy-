import streamlit as st
import google.generativeai as genai

# অ্যাপ কনফিগারেশন
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# আপনার API Key (সরাসরি কনফিগার করা)
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

try:
    genai.configure(api_key=API_KEY)
    # মডেল পরিবর্তন করা হয়েছে: gemini-pro (সব ভার্সনে সাপোর্ট করে)
    model = genai.GenerativeModel('gemini-pro') 
except Exception as e:
    st.error("API কনফিগারেশনে সমস্যা হয়েছে।")

# ডিজাইন (CSS)
st.markdown("""
    <style>
    .arabic-font { font-size: 35px !important; direction: rtl; text-align: center; background-color: #f0f2f6; padding: 20px; border-radius: 15px; border: 2px solid #2e7d32; }
    .tarkib-box { border: 2px solid #1b5e20; padding: 15px; border-radius: 10px; background-color: #ffffff; line-height: 1.8; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; font-weight: bold; height: 3em; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")
st.write("যেকোনো আরবি বাক্য লিখুন, AI এটি বিশ্লেষণ করে মাদরাসা স্টাইলে তারকিব করে দেবে।")

# ইনপুট
sentence = st.text_input("আপনার আরবি বাক্যটি এখানে দিন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if sentence:
        with st.spinner('AI বিশ্লেষণ করছে, দয়া করে অপেক্ষা করুন...'):
            try:
                # AI ইনস্ট্রাকশন
                prompt = f"""
                Analyze the following Arabic sentence and provide a detailed 'Tarkib' (Syntactic Analysis) in Bengali.
                Format:
                1. Individual word analysis (Ism, Fil, Harf).
                2. Explain relationships (Fail, Maful, Mudaaf, etc.).
                3. Final Jumla type.
                Arabic Sentence: {sentence}
                """
                
                response = model.generate_content(prompt)
                
                st.markdown(f'<div class="arabic-font">{sentence}</div>', unsafe_allow_html=True)
                st.markdown('<div class="tarkib-box">', unsafe_allow_html=True)
                st.subheader("বিশ্লেষণ ফলাফল:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"দুঃখিত, সমস্যাটি হলো: {str(e)}")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
