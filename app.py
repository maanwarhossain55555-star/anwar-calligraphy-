import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# পেজ সেটআপ
st.set_page_config(page_title="ANWAR CALLIGRAPHY", layout="centered")

# ফন্ট লোড করার ফাংশন
def get_font_base64(font_path):
    try:
        if os.path.exists(font_path):
            with open(font_path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
    except Exception:
        return None
    return None

# ফন্ট ফাইল নিশ্চিত করুন
font_filename = "MarhabanArabicDEMO-Bold.otf" 
font_base64 = get_font_base64(font_filename)

# সাইডবার বা মেনু হাইড করার জন্য এবং স্টাইল উন্নত করার জন্য CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button {
        width: 100%;
        background-color: #1a73e8;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #1557b0; border: none; }
    .stTextArea textarea {
        border-radius: 10px;
        background-color: #161b22;
        color: white;
        border: 1px solid #30363d;
    }
    h1 { color: #ffffff; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin-bottom: 0; }
    .brand-sub { text-align: center; color: #8b949e; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>ANWAR CALLIGRAPHY</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-sub'>Premium Arabic Typography Generator</p>", unsafe_allow_html=True)

# টেক্সট ইনপুট এরিয়া
user_input = st.text_area("আপনার আরবি টেক্সট এখানে লিখুন:", placeholder="مثال: بسم الله الرحمن الرحيم", height=100)

if not font_base64:
    st.error(f"'{font_filename}' খুঁজে পাওয়া যায়নি। দয়া করে এটি আপলোড করুন।")

# ক্যালিগ্রাফি আউটপুট এরিয়া
html_template = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        @font-face {{
            font-family: 'AnwarMarhaban';
            src: url(data:font/opentype;base64,{font_base64 if font_base64 else ""});
        }}
        body {{ background-color: #0e1117; margin: 0; display: flex; flex-direction: column; align-items: center; padding: 10px; }}
        
        #capture-area {{
            background-color: #000;
            padding: 60px 40px;
            border-radius: 12px;
            text-align: center;
            width: 90%;
            max-width: 700px;
            min-height: 250px;
            display: flex;
            justify-content: center;
            align-items: center;
            border: 1px solid #333;
            box-shadow: 0 10px 40px rgba(0,0,0,0.7);
        }}
        .calligraphy {{
            font-family: 'AnwarMarhaban', serif;
            font-size: 100px;
            color: #FFFFFF;
            margin: 0;
            line-height: 0.9;
            text-shadow: 0 0 10px rgba(255,255,255,0.1);
        }}
        .download-btn {{
            margin-top: 25px;
            padding: 12px 40px;
            background-color: #238636;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div id="capture-area">
        <div class="calligraphy">{user_input}</div>
    </div>
    <button class="download-btn" onclick="downloadImage()">Download PNG (HD)</button>
    <script>
        function downloadImage() {{
            const area = document.getElementById('capture-area');
            html2canvas(area, {{ backgroundColor: "#000000", scale: 4 }}).then(canvas => {{
                let link = document.createElement('a');
                link.download = 'Anwar_Calligraphy.png';
                link.href = canvas.toDataURL();
                link.click();
            }});
        }}
    </script>
</body>
</html>
"""

# জেনারেট বাটন
if st.button("ডিজাইন দেখুন"):
    if user_input.strip() == "":
        st.warning("আগে কিছু লিখুন!")
    else:
        components.html(html_template, height=500)

st.markdown("---")
st.caption("© 2026 ANWAR CALLIGRAPHY")
