import streamlit as st
import google.generativeai as genai
import os

# সরাসরি আপনার API Key
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# ১. সরাসরি কানেকশন সেটআপ
os.environ["GOOGLE_API_KEY"] = API_KEY
genai.configure(api_key=API_KEY)

# ২. পেজ সেটআপ
st.set_page_config(page_title="Arabic Tarkib AI", layout="centered")
st.title("🟢 সরাসরি আরবি তারকিব অ্যানালাইজার (AI)")
st.write("সরাসরি Gemini AI-এর মাধ্যমে আপনার আরবি বাক্যের তারকিব করুন।")

# ৩. ইনপুট বক্স
user_input = st.text_input("আরবি বাক্যটি এখানে লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("তারকিব বের করুন"):
    if user_input:
        with st.spinner('সরাসরি AI বিশ্লেষণ করছে...'):
            try:
                # কোনো ভার্সন ছাড়াই সরাসরি মডেল কল
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # সরাসরি আমার (AI) কাছে নির্দেশ
                prompt = f"Analyze the Arabic sentence: '{user_input}' and provide a detailed Tarkib in Bengali following Madrasa tradition (Dars-e-Nizami style)."
                
                response = model.generate_content(prompt)
                
                # ফলাফল প্রদর্শন
                st.success("বিশ্লেষণ সম্পন্ন!")
                st.info(response.text)
                
            except Exception as e:
                st.error(f"যান্ত্রিক ত্রুটি: {str(e)}")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
