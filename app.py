import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Arabic Calligraphy Generator", layout="centered")

# CSS দিয়ে ৩D শ্যাডো এফেক্ট তৈরি করা
st.markdown("""
<style>
    .calligraphy-title {
        text-align: center;
        font-family: 'Aref Ruqaa', serif;
        font-size: 30px;
        color: #fff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='calligraphy-title'>আরবি ক্যালিগ্রাফি জেনারেটর (3D Shadow)</h2>", unsafe_allow_html=True)

user_input = st.text_area("এখানে আরবি লিখুন:", placeholder="مثال: الجامعیة الغفوریة...", height=100)

# HTML ও CSS কোড যা ৩D শ্যাডো এফেক্ট দিবে
html_code = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Aref+Ruqaa:wght@700&family=Amiri+Quran&display=swap" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400..700&display=swap');
        
        body {{
            margin: 0;
            padding: 0;
            background-color: #000; /* ক্যালিগ্রাফির মতো ব্যাকগ্রাউন্ড */
        }}
        
        .calligraphy-box {{
            padding: 50px;
            text-align: center;
            min-height: 250px;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        
        .text-output {{
            font-family: 'Aref Ruqaa', serif; /* ফন্ট স্টাইল */
            font-size: 80px;
            color: #fff; /* ক্যালিগ্রাফির মতো সাদা রং */
            line-height: 1.4;
            word-spacing: 15px;
            
            /* ৩D শ্যাডো এফেক্ট দেওয়ার চেষ্টা */
            text-shadow: 
                -1px -1px 0 #333,
                1px -1px 0 #333,
                -1px 1px 0 #333,
                1px 1px 0 #333,
                0px 3px 0 #bbb,
                3px 0px 0 #bbb,
                -3px -3px 0 #fff,
                3px 3px 6px rgba(0,0,0,0.6);
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
