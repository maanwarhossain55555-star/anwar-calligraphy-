import streamlit as st
import google.generativeai as genai

# অ্যাপের সাধারণ সেটিংস
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")

# আপনার সরাসরি দেওয়া API Key
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# API কনফিগারেশন
try:
    genai.configure(api_key=API_KEY)
    # আপনার লাইব্রেরির জন্য সবচেয়ে স্থিতিশীল মডেল
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"API সংযোগে সমস্যা: {e}")

# মাদরাসা স্টাইলে ডিজাইন (CSS)
st.markdown("""
    <style>
    .arabic-text { font-size: 35px !important; direction: rtl; text-align: center; background-color: #f1f8e9; padding: 20px; border-radius: 10px; border: 2px solid #2e7d32; }
    .result-box { background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 5px solid #2e7d32; line-height: 1.8; color: #000; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 8px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")
st.write("যেকোনো আরবি বাক্য দিন, AI মাদরাসা স্টাইলে পূর্ণাঙ্গ তারকিব বের করে দেবে।")

# ইনপুট বক্স
user_input = st.text_input("আরবি বাক্যটি লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("পূর্ণাঙ্গ তারকিব বের করুন"):
    if user_input:
        with st.spinner('AI বিশ্লেষণ করছে, দয়া করে অপেক্ষা করুন...'):
            try:
                # সুনির্দিষ্ট ইনস্ট্রাকশন
                prompt = f"""
                Analyze this Arabic sentence: '{user_input}'
                Task: Provide a detailed 'Tarkib' (Syntactic Analysis) in Bengali.
                Method: Use standard Madrasa (Dars-e-Nizami) style.
                1. Word-by-word role.
                2. Final sentence type (Jumla).
                """
                
                response = model.generate_content(prompt)
                
                # ফলাফল প্রদর্শন
                st.markdown(f'<div class="arabic-text">{user_input}</div>', unsafe_allow_html=True)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("বিশ্লেষণ ফলাফল:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error("একটি সমস্যা হয়েছে। দয়া করে আপনার API Key সচল আছে কি না নিশ্চিত করুন।")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
