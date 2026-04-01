import streamlit as st
import google.generativeai as genai

# API কি সরাসরি সেট করা
API_KEY = "AIzaSyAX-YKKLj8BQ2d8HLk1v-LOoqskg2Wmp-o"

# অ্যাপের ইন্টারফেস
st.set_page_config(page_title="Arabic Tarkib AI", layout="wide")
st.title("🌍 গ্লোবাল আরবি তারকিব অ্যানালাইজার (AI)")

# ইনপুট ফিল্ড
user_input = st.text_input("আরবি বাক্যটি এখানে লিখুন:", placeholder="যেমন: نَصَرَ زَيْدٌ عَمْرًا")

if st.button("তারকিব বের করুন"):
    if user_input:
        with st.spinner('AI বিশ্লেষণ করছে...'):
            try:
                # গুগল এআই কনফিগার করা
                genai.configure(api_key=API_KEY)
                
                # সরাসরি মডেল কল করা (এটি v1beta এরর দিবে না)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"Analyze the Arabic sentence: '{user_input}' and provide a detailed Tarkib in Bengali Madrasa style."
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success("বিশ্লেষণ সম্পন্ন!")
                    st.write(response.text)
            except Exception as e:
                # এরর মেসেজ দেখালে সেটি সমাধান করতে সুবিধা হবে
                st.error(f"যান্ত্রিক ত্রুটি: {str(e)}")
    else:
        st.warning("আগে একটি আরবি বাক্য লিখুন।")
