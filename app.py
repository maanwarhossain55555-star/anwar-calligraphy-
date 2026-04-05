import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Pro Arabic Calligraphy", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    h2 { color: #ffffff; text-align: center; font-family: 'Arial'; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h2>Pro Arabic Calligraphy Generator</h2>", unsafe_allow_html=True)

user_input = st.text_area("আরবি লিখুন:", placeholder="এখানে আপনার আরবি টেক্সট লিখুন...", height=100)

# HTML, CSS এবং JS এর সমন্বয়ে ক্যালিগ্রাফি ও ডাউনলোড সিস্টেম
html_template = f"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        body {{ 
            background-color: #0e1117; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center; 
            font-family: 'Arial', sans-serif;
        }}
        
        #capture-area {{
            background: black;
            padding: 60px 80px;
            border-radius: 15px;
            display: inline-block;
            text-align: center;
            border: 1px solid #333;
        }}

        .calligraphy {{
            font-family: 'Amiri Quran', serif;
            font-size: 90px;
            color: #FFFFFF;
            line-height: 1.2;
            margin: 0;
            /* 3D Depth Shadow */
            text-shadow: 
                0 1px 0 #ccc, 0 2px 0 #c9c9c9, 0 3px 0 #bbb, 
                0 4px 0 #b9b9b9, 0 5px 0 #aaa, 0 6px 1px rgba(0,0,0,.1), 
                0 0 5px rgba(0,0,0,.1), 0 1px 3px rgba(0,0,0,.3), 
                0 3px 5px rgba(0,0,0,.2), 0 5px 10px rgba(0,0,0,.25), 
                0 10px 10px rgba(0,0,0,.2), 0 20px 20px rgba(0,0,0,.15);
        }}

        .btn-download {{
            margin-top: 20px;
            padding: 12px 25px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }}
        .btn-download:hover {{ background-color: #45a049; }}
    </style>
</head>
<body>

    <div id="capture-area">
        <p class="calligraphy">{user_input}</p>
    </div>

    <button class="btn-download" onclick="downloadImage()">Download as Photo (HD)</button>

    <script>
        function downloadImage() {{
            const area = document.getElementById('capture-area');
            html2canvas(area, {{ 
                backgroundColor: "#000000",
                scale: 3 // হাই কোয়ালিটির জন্য স্কেল বাড়ানো হয়েছে
            }}).then(canvas => {{
                let link = document.createElement('a');
                link.download = 'calligraphy_design.png';
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
        st.error("দয়া করে আগে কিছু লিখুন!")
    else:
        components.html(html_template, height=550, scrolling=True)

st.info("দ্রষ্টব্য: এটি ওয়েব ফন্ট ব্যবহার করে সর্বোচ্চ ৩D লুক দেওয়ার চেষ্টা করে। হুবহু AI ইমেজের মতো রেজাল্ট পেতে গ্রাফিক ডিজাইন বা AI ইমেজ জেনারেটরই সেরা মাধ্যম।")
