import streamlit as st
import streamlit.components.v1 as components

# পেজ সেটআপ
st.set_page_config(page_title="Arabic Calligraphy Generator", layout="centered")

st.markdown("<h2 style='text-align: center;'>আরবি ক্যালিগ্রাফি জেনারেটর</h2>", unsafe_allow_html=True)

# আরবি ইনপুট নেওয়ার বক্স
user_input = st.text_area("এখানে আরবি লিখুন:", placeholder="مثال: الجامعیة الغفوریة...", height=100)

# HTML ও CSS কোড যা ক্যালিগ্রাফি তৈরি করবে
html_code = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Aref+Ruqaa:wght@700&display=swap" rel="stylesheet">
    <style>
        .calligraphy-box {{
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            border: 2px solid #eee;
            text-align: center;
            min-height: 200px;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        .text-output {{
            font-family: 'Amiri Quran', serif;
            font-size: 70px;
            color: black;
            word-wrap: break-word;
            line-height: 1.5;
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

# জেনারেট বাটন
if st.button("ক্যালিগ্রাফি জেনারেট করুন"):
    if user_input.strip() == "":
        st.warning("অনুগ্রহ করে আগে কিছু আরবি টেক্সট লিখুন।")
    else:
        # HTML কম্পোনেন্ট রেন্ডার করা
        components.html(html_code, height=400)

st.info("দ্রষ্টব্য: এই কোডটি 'Amiri' ক্যালিগ্রাফি ফন্ট ব্যবহার করে আপনার টেক্সটকে শৈল্পিক রূপ দেয়।")
