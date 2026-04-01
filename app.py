import streamlit as st
import google.generativeai as genai

# অ্যাপের সাধারণ সেটিংস
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# আপনার সরাসরি দেওয়া API Key
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# ডিজাইন (CSS)
st.markdown("""
    <style>
    .arabic-text { font-size: 35px !important; direction: rtl; text-align: center; background-color: #f1f8e9; padding: 20px; border-radius: 10px; border: 2px solid #2e7d32; }
    .result-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; line-height: 1.8; color: #000; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")

# ইনপুট বক্স
user_input = st.text_input("আরবি বাক্যটি লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if user_input:
        with st.spinner('AI বিশ্লেষণ করছে...'):
            try:
                # API কনফিগারেশন সরাসরি এখানে করা হয়েছে
                genai.configure(api_key=API_KEY)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # সুনির্দিষ্ট ইনস্ট্রাকশন
                prompt = f"Analyze this Arabic sentence: '{user_input}'. Provide a detailed Tarkib in Bengali using Madrasa style."
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.markdown(f'<div class="arabic-text">{user_input}</div>', unsafe_allow_html=True)
                    st.markdown('<div class="result-box">', unsafe_allow_html=True)
                    st.write(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.error("AI কোনো উত্তর দিতে পারেনি।")
                    
            except Exception as e:
                # এররটি পরিষ্কারভাবে দেখানোর জন্য
                st.error(f"দুঃখিত, সমস্যাটি হলো: {str(e)}")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
