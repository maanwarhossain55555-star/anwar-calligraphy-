import streamlit as st
import streamlit.components.v1 as components

# পেজ সেটআপ
st.set_page_config(page_title="ANWAR CALLIGRAPHY", layout="centered")

# ইন্টারফেস ডিজাইন (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button {
        width: 100%; background-color: #1a73e8; color: white;
        font-weight: bold; border-radius: 8px; height: 3.5em; border: none;
    }
    .stTextArea textarea {
        border-radius: 10px; background-color: #161b22; color: white;
        border: 1px solid #30363d; text-align: right; font-size: 18px;
    }
    /* টাইটেল স্টাইল */
    h1 { 
        color: #ffffff; 
        text-align: center; 
        margin-bottom: 0px; 
        white-space: nowrap; /* টাইটেল এক লাইনে রাখার জন্য */
    }
    .sub-brand { text-align: center; color: #8b949e; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>ANWAR CALLIGRAPHY</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-brand'>Premium Arabic Calligraphy Generator</p>", unsafe_allow_html=True)

# টেক্সট ইনপুট
user_input = st.text_area("আপনার আরবি টেক্সট এখানে লিখুন:", placeholder="مثال: بسم الله الرحمن الرحيم", height=100)

# আউটপুট টেমপ্লেট
html_template = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@700&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        body {{ 
            background-color: #0e1117; 
            margin: 0; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            overflow: hidden;
        }}
        
        #capture-area {{
            background-color: #000; 
            padding: 50px 40px; 
            border-radius: 15px;
            text-align: center; 
            width: 90vw; /* স্ক্রিনের চওড়া অনুযায়ী অ্যাডজাস্ট হবে */
            max-width: 800px;
            min-height: 200px;
            display: flex; 
            justify-content: center; 
            align-items: center;
            border: 1px solid #333; 
            box-shadow: 0 25px 60px rgba(0,0,0,0.9);
            overflow: hidden;
        }}

        .calligraphy {{
            font-family: 'Reem+Kufi', sans-serif; 
            font-size: 8vw; /* স্ক্রিন ছোট হলে লেখাও ছোট হবে */
            max-font-size: 100px;
            color: #FFFFFF;
            margin: 0; 
            line-height: 1.2; 
            text-shadow: 0 0 15px rgba(255,255,255,0.1);
            white-space: nowrap; /* লেখা এক লাইনে রাখার জন্য প্রধান কমান্ড */
        }}

        /* বড় স্ক্রিনের জন্য ফন্ট সাইজ কন্ট্রোল */
        @media (min-width: 800px) {{
            .calligraphy {{ font-size: 100px; }}
        }}

        .download-btn {{
            margin-top: 30px; padding: 14px 50px; background-color: #238636;
            color: white; border: none; border-radius: 30px; cursor: pointer;
            font-size: 16px; font-weight: bold; transition: 0.3s;
        }}
    </style>
</head>
<body>
    <div id="capture-area">
        <div class="calligraphy">{user_input}</div>
    </div>
    <button class="download-btn" onclick="downloadImage()">Download HD Image</button>
    
    <script>
        function downloadImage() {{
            const area = document.getElementById('capture-area');
            // ডাউনলোড করার সময় যাতে পুরোটা আসে সেজন্য width ফিক্সড করা হলো
            html2canvas(area, {{ 
                backgroundColor: "#000000", 
                scale: 3,
                width: area.scrollWidth,
                height: area.scrollHeight
            }}).then(canvas => {{
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

if st.button("ডিজাইন তৈরি করুন"):
    if not user_input.strip():
        st.warning("আগে কিছু লিখুন!")
    else:
        components.html(html_template, height=550, scrolling=False)

st.markdown("---")
st.caption("© 2026 ANWAR CALLIGRAPHY")
