import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# পেজ টাইটেল এবং আইকন সেটআপ
st.set_page_config(page_title="ANWAR CALLIGRAPHY", layout="centered")

# ফন্ট লোড করার ফাংশন
def get_font_base64(font_path):
    try:
        if os.path.exists(font_path):
            with open(font_path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()
    except Exception as e:
        return None
    return None

# আপনার আপলোড করা ফন্ট ফাইলের নাম
font_filename = "MarhabanArabicDEMO-Bold.otf" 
font_base64 = get_font_base64(font_filename)

# অ্যাপের ইন্টারফেস টাইটেল
st.markdown("<h1 style='text-align: center; color: white; font-family: sans-serif;'>ANWAR CALLIGRAPHY</h1>", unsafe_allow_html=True)

user_input = st.text_area("আরবি টেক্সট লিখুন:", placeholder="مثال: بسم الله الرحمن الرحيم", height=100)

if not font_base64:
    st.error(f"'{font_filename}' ফাইলটি পাওয়া যায়নি। এটি আপনার GitHub রিপোজিটরিতে আপলোড করা আছে কি না নিশ্চিত করুন।")

# ডিজাইন টেমপ্লেট
html_template = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        @font-face {{
            font-family: 'MarhabanFont';
            src: url(data:font/opentype;base64,{font_base64 if font_base64 else ""});
        }}
        
        body {{ 
            background-color: #0e1117; 
            margin: 0; 
            display: flex; 
            flex-direction: column; 
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        
        #capture-area {{
            background-color: #000;
            padding: 60px;
            border-radius: 15px;
            text-align: center;
            min-width: 600px;
            min-height: 300px;
            display: flex;
            justify-content: center;
            align-items: center;
            border: 2px solid #333;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}

        .calligraphy {{
            font-family: 'MarhabanFont', serif;
            font-size: 120px;
            color: #FFFFFF;
            margin: 0;
            padding: 0;
            line-height: 0.8; /* লেখা যাতে বেশি নিচে না নামে */
            display: inline-block;
            text-shadow: 2px 2px 10px rgba(255,255,255,0.1);
        }}

        .download-btn {{
            margin-top: 30px;
            padding: 15px 40px;
            background-color: #1a73e8;
            color: white;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            transition: 0.3s;
        }}
        .download-btn:hover {{
            background-color: #1557b0;
            transform: scale(1.05);
        }}
    </style>
</head>
<body>

    <div id="capture-area">
        <div class="calligraphy">{user_input}</div>
    </div>

    <button class="download-btn" onclick="downloadImage()">Download HD Calligraphy</button>

    <script>
        function downloadImage() {{
            const area = document.getElementById('capture-area');
            html2canvas(area, {{ 
                backgroundColor: "#000000",
                scale: 4, /* হাই-রেজোলিউশন ছবির জন্য */
                logging: false,
                useCORS: true
            }}).then(canvas => {{
                let link = document.createElement('a');
                link.download = 'Anwar_Calligraphy.png';
                link.href = canvas.toDataURL("image/png");
                link.click();
            }});
        }}
    </script>
</body>
</html>
"""

if st.button("ডিজাইন তৈরি করুন"):
    if user_input.strip() == "":
        st.warning("আগে কিছু আরবি লিখুন!")
    else:
        # কম্পোনেন্ট হাইট বাড়ানো হয়েছে যাতে কোনো অংশ না কাটে
        components.html(html_template, height=600)

st.markdown("---")
st.caption("© 2026 ANWAR CALLIGRAPHY | Powered by Marhaban Font")
