import streamlit as st
import google.generativeai as genai

# সরাসরি আপনার এপিআই কী
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# ১. সরাসরি সংযোগ স্থাপন
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# ২. পেজ ডিজাইন
st.set_page_config(page_title="Arabic Tarkib AI", layout="centered")
st.title("🟢 সরাসরি আরবি তারকিব অ্যানালাইজার (AI)")

# ৩. ইনপুট বক্স
user_input = st.text_input("আরবি বাক্যটি লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("তারকিব বের করুন"):
    if user_input:
        with st.spinner('সরাসরি AI বিশ্লেষণ করছে...'):
            try:
                # সরাসরি আমার কাছে (Gemini) নির্দেশ পাঠানো
                prompt = f"Analyze the Arabic sentence: '{user_input}' and provide a detailed Tarkib in Bengali following Madrasa tradition (Dars-e-Nizami style)."
                response = model.generate_content(prompt)
                
                # রেজাল্ট প্রদর্শন
                st.success("বিশ্লেষণ সম্পন্ন!")
                st.markdown(f"### তারকিব বিশ্লেষণ:\n{response.text}")
                
            except Exception as e:
                # এররটি পরিষ্কারভাবে দেখাবে যাতে আমরা সমাধান করতে পারি
                st.error(f"যান্ত্রিক ত্রুটি: {str(e)}")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
