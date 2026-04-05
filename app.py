import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Arabic Calligraphy Generator", layout="centered")

st.markdown("<h2 style='text-align: center;'>আরবি ক্যালিগ্রাফি জেনারেটর (Thuluth Style)</h2>", unsafe_allow_html=True)

user_input = st.text_area("এখানে আরবি লিখুন:", placeholder="مثال: الجامعیة الغفوریة...", height=100)

# এখানে আমরা গুগল ফন্টের 'Aref Ruqaa' এবং 'Amiri' ব্যবহার করছি যা ক্যালিগ্রাফির জন্য সেরা
html_code = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@700&family=Amiri+Quran&display=swap" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400..700&display=swap');
        
        .calligraphy-box {{
            background-color: white;
            padding: 50px;
            border-radius: 15px;
            text-align: center;
            min-height: 250px;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.05);
        }}
        .text-output {{
            /* Thuluth/Diwani লুকের জন্য Aref Ruqaa অথবা Amiri Quran সবচেয়ে ভালো */
            font-family: 'Aref Ruqaa', serif; 
            font-size: 85px;
            color: #1a1a1a;
            line-height: 1.4;
            word-spacing: 10px;
            letter-spacing: -1px; /* অক্ষরগুলো কাছাকাছি আনার জন্য */
        }}
    </style>
</head>
<body>
    <div class="calligraphy-box">
        <div class="text-output">{user_input}</div>
    </div>
</body>
</html>
"""

if st.button("ক্যালিগ্রাফি জেনারেট করুন"):
    if user_input.strip() == "":
        st.warning("অনুগ্রহ করে কিছু লিখুন।")
    else:
        components.html(html_code, height=450)

st.markdown("---")
st.caption("টিপস: আপনি যদি হুবহু 'Diwani Thuluth' এর মতো আরও ঘন ক্যালিগ্রাফি চান, তবে আপনার পিসিতে থাকা ঐ নির্দিষ্ট .ttf ফন্টটি GitHub-এ আপলোড করে সেটি CSS-এ লিঙ্ক করতে হবে।")
