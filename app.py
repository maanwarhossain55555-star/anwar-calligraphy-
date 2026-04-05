import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Premium Arabic Calligraphy", layout="centered")

# CSS দিয়ে ইন্টারফেস সুন্দর করা
st.markdown("""
    <style>
    .stTextArea textarea { font-size: 18px !important; text-align: right; }
    .main { background-color: #0e1117; }
    </style>
    """, unsafe_allow_html=True)

st.title("Arabic Thuluth Calligraphy Generator")

user_input = st.text_area("আরবি টেক্সট লিখুন (চিহ্নসহ লিখলে বেশি সুন্দর হবে):", 
                          placeholder="مثال: اَلْجَامِعَةُ الْغَفُوْرِيَّة...", height=120)

# ক্যালিগ্রাফি ও ডাউনলোড লজিক
html_template = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Aref+Ruqaa:wght@700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        body {{ background-color: #0e1117; display: flex; flex-direction: column; align-items: center; }}
        
        #canvas-area {{
            background: #000;
            padding: 80px;
            border-radius: 10px;
            text-align: center;
            border: 2px solid #222;
            width: fit-content;
            max-width: 90%;
        }}

        .thuluth-text {{
            /* Amiri Quran ফন্টটি চিহ্ন বা Tashkeel সবচেয়ে সুন্দরভাবে দেখায় */
            font-family: 'Amiri Quran', serif;
            font-size: 100px;
            color: #fff;
            line-height: 1.5;
            letter-spacing: 1px;
            /* আপনার ছবির মতো হালকা ৩D লুক */
            text-shadow: 2px 2px 0px #444, 4px 4px 8px rgba(0,0,0,0.8);
        }}

        .download-btn {{
            margin-top: 30px;
            padding: 12px 30px;
            background: #1e88e5;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }}
    </style>
</head>
<body>

    <div id="canvas-area">
        <div class="thuluth-text">{user_input}</div>
    </div>

    <button class="download-btn" onclick="takeScreenshot()">ইমেজ ডাউনলোড করুন (HD)</button>

    <script>
        function takeScreenshot() {{
            const area = document.getElementById('canvas-area');
            html2canvas(area, {{ scale: 3, backgroundColor: "#000" }}).then(canvas => {{
                let link = document.createElement('a');
                link.download = 'calligraphy.png';
                link.href = canvas.toDataURL();
                link.click();
            }});
        }}
    </script>
</body>
</html>
"""

if st.button("ক্যালিগ্রাফি ডিজাইন দেখুন"):
    if user_input:
        components.html(html_template, height=600, scrolling=True)
    else:
        st.error("কিছু লিখুন!")

st.markdown("---")
st.info("💡 **পরামর্শ:** হুবহু আপনার প্রথম ছবির মতো রেজাল্ট পেতে হলে টাইপ করার সময় হরকত বা চিহ্ন (যের, জবর, পেশ) ব্যবহার করুন। ক্যালিগ্রাফি ফন্ট এই চিহ্নগুলো পেলেই কেবল পূর্ণাঙ্গ রূপ পায়।")
