import streamlit as st
import google.generativeai as genai

# ১. প্রাথমিক সেটিংস
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# ২. আপনার সরাসরি দেওয়া API Key
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# ৩. এআই কনফিগারেশন (যান্ত্রিক ত্রুটি এড়াতে নতুন পদ্ধতি)
try:
    genai.configure(api_key=API_KEY)
    # সঠিক মডেল খুঁজে নেওয়া
    model = genai.GenerativeModel('gemini-1.5-flash-latest') 
except Exception as e:
    st.error(f"এআই সংযোগে সমস্যা: {e}")

# ৪. মাদরাসা নোটের মতো ডিজাইন
st.markdown("""
    <style>
    .arabic-text { font-size: 35px !important; direction: rtl; text-align: center; background-color: #f1f8e9; padding: 20px; border-radius: 10px; border: 2px solid #2e7d32; }
    .result-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; color: black; line-height: 1.8; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; font-weight: bold; border-radius: 10px; height: 50px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")

# ৫. ইনপুট বক্স
user_input = st.text_input("আরবি বাক্যটি এখানে লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if user_input:
        with st.spinner('AI বিশ্লেষণ করছে, দয়া করে একটু অপেক্ষা করুন...'):
            try:
                # এআই-কে নির্দেশ দেওয়া
                prompt = f"Analyze the Arabic sentence: '{user_input}' and provide a detailed Tarkib in Bengali following Madrasa tradition (Dars-e-Nizami style)."
                response = model.generate_content(prompt)
                
                # ফলাফল দেখানো
                st.markdown(f'<div class="arabic-text">{user_input}</div>', unsafe_allow_html=True)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("বিশ্লেষণ ফলাফল:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                # এরর মেসেজ সহজ করা
                st.error("দুঃখিত, সংযোগে সামান্য সমস্যা হয়েছে। দয়া করে আবার চেষ্টা করুন।")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
