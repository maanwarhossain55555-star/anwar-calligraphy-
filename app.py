import streamlit as st
import google.generativeai as genai

# সরাসরি আপনার এপিআই কী
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# ১. সরাসরি সংযোগ স্থাপন (সবচেয়ে সহজ পদ্ধতি)
genai.configure(api_key=API_KEY)

# ২. পেজ সেটআপ
st.set_page_config(page_title="Arabic Tarkib AI")
st.title("🟢 সরাসরি আরবি তারকিব অ্যানালাইজার (AI)")

# ৩. ইনপুট বক্স
user_input = st.text_input("আরবি বাক্যটি লিখুন:")

if st.button("তারকিব বের করুন"):
    if user_input:
        with st.spinner('সরাসরি AI বিশ্লেষণ করছে...'):
            try:
                # কোনো ভার্সন উল্লেখ না করে সরাসরি মডেল কল করা
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # সরাসরি আমার (Gemini) জন্য স্পষ্ট নির্দেশ
                prompt = f"Analyze the Arabic sentence: '{user_input}' and provide a detailed Tarkib in Bengali Madrasa style."
                
                response = model.generate_content(prompt)
                
                # রেজাল্ট প্রদর্শন
                st.success("বিশ্লেষণ সম্পন্ন!")
                st.write(response.text)
                
            except Exception as e:
                # এরর আসলে এটি সরাসরি সমাধান বলে দিবে
                st.error(f"যান্ত্রিক ত্রুটি: {str(e)}")
                st.info("টিপস: যদি মডেল খুঁজে না পায়, তবে GitHub-এ requirements.txt ফাইলটি চেক করুন।")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
